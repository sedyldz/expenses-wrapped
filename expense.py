import glob
import os
import pandas as pd
# Adjusting the function to handle Turkish-specific case conversion
import unicodedata
# Loads an Excel expense file, cleans and prepares the data, 
# translates expense keywords to Turkish, categorizes expenses based on keywords,
# and saves the categorized expenses to a new CSV file.

current_dir = os.getcwd()

def turkish_lower(s):
    return unicodedata.normalize('NFKC', s).replace('İ', 'i').replace('Ş', 'ş').lower()


# Translating the keywords to Turkish for better categorization
# Updated keywords in Turkish
keywords = {
    "Food & Drink": ["a.ç.t. dürüm ve meze", "arkestra", "bakery", "bakes", "bakkal", "bim","bordel", "cagrim", "dondurma", "ebsm et balik", "firin", "gida","gozde sarkuteri", "harman firin", "kafe", "kahve", "lokanta", "market","cafe","marmaris büfe", "migros", "mill cafe", "minimal kahve mutfak", "mopas", "mudavim", "müdavim lokantasi", "narbakery", "nicel bakes scoops", "parantez panayir yerigida", "perakende", "pinar dondurma", "rest", "restaurant", "restoran", "salipazari", "salipazari yavuzun y", "sarkuteri","şarküteri","su urunleri", "süpermarket", "tove gida", "unlu mamüller", "unlumamüller", "mc donalds", "çağrım unlu mamuller", "çağrım unlu mamüller","sour","sweet","benazio","kahve","mutfak","village","şok","haci bekir","kafe","yemek","burger","caffe","happy center","tekel","ekşihane","gelato","sorbet","kuruyemis","kuruyemiş","haribo"],
    "Home+Health": ["eczane", "sağlık", "fatura", "ev", "kira", "iski su", "enerjisa ayesaş","ikea","bauhaus","türk telekom mobil", "turkcell superonline","carrefour","kozmetik"],
    "Clothes+Beauty+Utilities": ["giyim", "kıyafet", "moda", "güzellik", "kuaför","beymen","vakko","zorlu","atasun","kuvars","brooks brothers","barcin","h&m","cos","spor","ralph lauren","decathlon","tekstil","massimo","zara","sportive","mudo","mango","apple store","levis","oysho","trendyol","gratis","benetton"],
    "Entertainment": ["sinema", "film", "eğlence", "oyun", "konser","etkinlik","passo","müzik","muzik"],
    "Travel": ["ita","fr","prt","seyahat", "uçuş", "otel", "tren", "otobüs","uber","airbnb","moov","belbim","booking","bitaksi","takside","lisboa","sabiha gökçen"],
    "Subscription": ["spotify", "netflix", "prime", "hbo", "patreon","apple.com/bill","google"],
    "Tax": ["vergi","v.d."],
    "Other": []  # No specific keywords for 'Other'; it's a default category
}



# Function to categorize each expense based on the Turkish operation description
def categorize_expense_tr(operation):
    operation = turkish_lower(operation)
    #print(operation)
    if "iade" in operation or "hesaptan ödeme" in operation:
        return "Skipped" 
    for category, category_keywords in keywords.items():
        if any(keyword in operation for keyword in category_keywords):
            return category           
    return "Other"

search_path = os.path.join("expenses", 'expenses_*.xlsx')
files = glob.glob(search_path)
for f in files:
    filename = os.path.basename(f).split('.')[0]
    extension = ".csv"    
    categorized_file = "categorized_" + filename + extension
    expenses_df = pd.read_excel(f)

    # Rename the columns with English headers, adding a second header
    expenses_df.columns = ['operation', 'amount', 'currency', 'date', 'bonus', 'description']
    # Drop the first row which contains the original headers in Turkish
    expenses_df = expenses_df.drop(expenses_df.index[0])
    # Drop the 'bonus' column, axis 1 deletes column instead of row
    expenses_df = expenses_df.drop('bonus', axis=1)
    expenses_df.head()

    # Apply the new categorization function to the dataframe
    expenses_df['category'] = expenses_df['operation'].apply(categorize_expense_tr)

    # Save the updated dataframe to a new CSV file
    updated_file_path_tr = categorized_file
    expenses_df.to_csv(updated_file_path_tr, index=False)

    updated_file_path_tr