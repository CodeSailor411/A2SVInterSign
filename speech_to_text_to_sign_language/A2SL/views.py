from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles import finders
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

@login_required(login_url="login")
def animation_view(request):
    if request.method == 'POST':
        text = request.POST.get('sen', '')

        # Tokenizing and processing the text
        text = text.lower()
        words = word_tokenize(text)
        tagged = nltk.pos_tag(words)
        
        # Tense identification
        tense = {
            "future": len([word for word in tagged if word[1] == "MD"]),
            "present": len([word for word in tagged if word[1] in ["VBP", "VBZ", "VBG"]]),
            "past": len([word for word in tagged if word[1] in ["VBD", "VBN"]]),
            "present_continuous": len([word for word in tagged if word[1] == "VBG"])
        }

        # Stopwords to remove
        stop_words = set(stopwords.words('english'))

        # Lemmatizing and filtering text
        lemmatizer = WordNetLemmatizer()
        filtered_text = []
        for w, p in zip(words, tagged):
            if w not in stop_words:
                if p[1] in ['VBG', 'VBD', 'VBZ', 'VBN', 'NN']:
                    filtered_text.append(lemmatizer.lemmatize(w, pos='v'))
                elif p[1] in ['JJ', 'JJR', 'JJS', 'RBR', 'RBS']:
                    filtered_text.append(lemmatizer.lemmatize(w, pos='a'))
                else:
                    filtered_text.append(lemmatizer.lemmatize(w))
        
        # Adding tense indicators
        words = filtered_text
        if tense["past"] > 0:
            words = ["Before"] + words
        elif tense["future"] > 0 and "Will" not in words:
            words = ["Will"] + words
        elif tense["present_continuous"] > 0:
            words = ["Now"] + words

        # File handling for animations
        final_words = []
        for w in words:
            path = f"{w}.mp4"
            f = finders.find(path)
            if not f:
                final_words.extend(list(w))  # Split word into characters
            else:
                final_words.append(w)

        return render(request, 'animation.html', {'words': final_words, 'text': text})
    else:
        return render(request, 'animation.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('animation')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', 'animation')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("home")
