# bookshelf/forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import escape
from .models import Book

class ExampleForm(forms.Form):
    """
    Example form demonstrating secure form practices including:
    - Field validation
    - Input sanitization
    - CSRF protection (automatically included in Django forms)
    """
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        }),
        error_messages={
            'required': 'Name is required',
            'max_length': 'Name cannot exceed 100 characters'
        }
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        }),
        error_messages={
            'required': 'Email is required',
            'invalid': 'Please enter a valid email address'
        }
    )
    
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your message',
            'rows': 4
        }),
        error_messages={
            'required': 'Message is required'
        }
    )
    
    def clean_name(self):
        """Sanitize and validate the name field"""
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise ValidationError("Name cannot be empty")
        
        # Sanitize input to prevent XSS
        sanitized_name = escape(name)
        
        # Additional validation - only allow letters and spaces
        if not all(c.isalpha() or c.isspace() for c in name):
            raise ValidationError("Name can only contain letters and spaces")
        
        return sanitized_name
    
    def clean_message(self):
        """Sanitize and validate the message field"""
        message = self.cleaned_data.get('message', '').strip()
        if not message:
            raise ValidationError("Message cannot be empty")
        
        # Sanitize input but preserve line breaks for textarea
        sanitized_message = escape(message)
        
        # Limit message length
        if len(message) > 1000:
            raise ValidationError("Message cannot exceed 1000 characters")
        
        return sanitized_message

class BookForm(forms.ModelForm):
    """
    Secure form for creating and editing books with validation
    and input sanitization to prevent SQL injection and XSS attacks.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'description', 'is_available']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name'
            }),
            'published_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ISBN (13 digits)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book description',
                'rows': 4
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'is_available': 'Available for borrowing'
        }
        error_messages = {
            'title': {
                'required': 'Book title is required',
                'max_length': 'Title cannot exceed 200 characters'
            },
            'author': {
                'required': 'Author name is required',
                'max_length': 'Author name cannot exceed 100 characters'
            },
            'isbn': {
                'required': 'ISBN is required',
                'unique': 'A book with this ISBN already exists'
            }
        }
    
    def clean_title(self):
        """Sanitize and validate the title field"""
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise ValidationError("Book title is required")
        
        # Sanitize input to prevent XSS
        sanitized_title = escape(title)
        
        return sanitized_title
    
    def clean_author(self):
        """Sanitize and validate the author field"""
        author = self.cleaned_data.get('author', '').strip()
        if not author:
            raise ValidationError("Author name is required")
        
        # Sanitize input to prevent XSS
        sanitized_author = escape(author)
        
        return sanitized_author
    
    def clean_isbn(self):
        """Validate ISBN format"""
        isbn = self.cleaned_data.get('isbn', '').strip()
        
        # Remove any hyphens or spaces
        clean_isbn = isbn.replace('-', '').replace(' ', '')
        
        # Validate ISBN length (10 or 13 digits)
        if len(clean_isbn) not in [10, 13]:
            raise ValidationError("ISBN must be 10 or 13 digits")
        
        # Validate that it contains only digits
        if not clean_isbn.isdigit():
            raise ValidationError("ISBN must contain only digits")
        
        return clean_isbn
    
    def clean_description(self):
        """Sanitize the description field"""
        description = self.cleaned_data.get('description', '').strip()
        
        if description:
            # Sanitize input to prevent XSS while preserving formatting
            sanitized_description = escape(description)
            return sanitized_description
        
        return description

class BookSearchForm(forms.Form):
    """
    Secure search form with validation to prevent SQL injection
    through search functionality.
    """
    search_query = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by title, author, or ISBN',
            'aria-label': 'Search books'
        }),
        error_messages={
            'max_length': 'Search query cannot exceed 100 characters'
        }
    )
    
    def clean_search_query(self):
        """Sanitize search query to prevent XSS and SQL injection"""
        query = self.cleaned_data.get('search_query', '').strip()
        
        if query:
            # Sanitize input to prevent XSS
            sanitized_query = escape(query)
            
            # Additional validation to prevent potential SQL injection patterns
            sql_injection_patterns = [
                ';', '--', '/*', '*/', 'union', 'select', 'insert', 
                'update', 'delete', 'drop', 'exec', 'xp_'
            ]
            
            for pattern in sql_injection_patterns:
                if pattern in query.lower():
                    raise ValidationError("Invalid search query")
            
            return sanitized_query
        
        return query

class ContactForm(forms.Form):
    """
    Additional example form for contact purposes
    demonstrating different field types and validation.
    """
    SUBJECT_CHOICES = [
        ('', 'Select a subject'),
        ('general', 'General Inquiry'),
        ('technical', 'Technical Support'),
        ('suggestion', 'Suggestion'),
        ('complaint', 'Complaint')
    ]
    
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    urgency = forms.ChoiceField(
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        initial='medium'
    )
    
    attachment = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        help_text='Maximum file size: 2.5MB'
    )
    
    def clean_attachment(self):
        """Validate file uploads"""
        attachment = self.cleaned_data.get('attachment')
        
        if attachment:
            # Check file size
            if attachment.size > 2.5 * 1024 * 1024:  # 2.5MB
                raise ValidationError("File size must not exceed 2.5MB")
            
            # Check file type
            valid_extensions = ['.pdf', '.doc', '.docx', '.txt', '.jpg', '.png']
            if not any(attachment.name.lower().endswith(ext) for ext in valid_extensions):
                raise ValidationError("Unsupported file type")
        
        return attachment