import json
import os
from datetime import datetime
from collections import Counter

class DreamVista:
    def __init__(self, data_file='dream_vista_data.json'):
        self.data_file = data_file
        self.data = {
            'symbols': [],
            'dreams': [],
            'interpretations': []
        }
        self.load_data()
        
    def load_data(self):
        """Load data from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.data = json.load(f)
                print("✓ Data loaded successfully")
            else:
                print("✓ Creating new data file")
                self.populate_initial_symbols()
                self.save_data()
        except Exception as e:
            print(f"✗ Error loading data: {e}")
            self.populate_initial_symbols()
    
    def save_data(self):
        """Save data to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2, default=str)
            return True
        except Exception as e:
            print(f"✗ Error saving data: {e}")
            return False
    
    def populate_initial_symbols(self):
        """Add initial dream symbols"""
        symbols = [
            {
                'id': 1,
                'symbol': 'flying',
                'meaning': 'Freedom, ambition, desire to escape limitations, spiritual elevation',
                'emotional_tone': 'positive',
                'category': 'movement',
                'keywords': 'soar, float, levitate, air, wings'
            },
            {
                'id': 2,
                'symbol': 'falling',
                'meaning': 'Loss of control, anxiety, insecurity, fear of failure',
                'emotional_tone': 'negative',
                'category': 'movement',
                'keywords': 'drop, plunge, descend, crash'
            },
            {
                'id': 3,
                'symbol': 'water',
                'meaning': 'Emotions, unconscious mind, purification, life force',
                'emotional_tone': 'neutral',
                'category': 'nature',
                'keywords': 'ocean, sea, river, rain, flood, swimming'
            },
            {
                'id': 4,
                'symbol': 'fire',
                'meaning': 'Passion, transformation, anger, destruction, purification',
                'emotional_tone': 'intense',
                'category': 'element',
                'keywords': 'flames, burning, heat, smoke, blaze'
            },
            {
                'id': 5,
                'symbol': 'death',
                'meaning': 'Transformation, ending, new beginning, fear of change',
                'emotional_tone': 'transformative',
                'category': 'life',
                'keywords': 'dying, funeral, corpse, grave'
            },
            {
                'id': 6,
                'symbol': 'snake',
                'meaning': 'Transformation, healing, hidden fears, temptation, wisdom',
                'emotional_tone': 'mysterious',
                'category': 'animal',
                'keywords': 'serpent, reptile, viper, python'
            },
            {
                'id': 7,
                'symbol': 'teeth falling out',
                'meaning': 'Anxiety, powerlessness, aging, communication issues',
                'emotional_tone': 'anxious',
                'category': 'body',
                'keywords': 'tooth, dental, losing teeth, mouth'
            },
            {
                'id': 8,
                'symbol': 'chase',
                'meaning': 'Avoidance, running from problems, fear, anxiety',
                'emotional_tone': 'stressful',
                'category': 'action',
                'keywords': 'pursued, running, escape, hunted'
            },
            {
                'id': 9,
                'symbol': 'naked in public',
                'meaning': 'Vulnerability, fear of exposure, authenticity, shame',
                'emotional_tone': 'vulnerable',
                'category': 'social',
                'keywords': 'nude, exposed, undressed, bare'
            },
            {
                'id': 10,
                'symbol': 'exam or test',
                'meaning': 'Performance anxiety, feeling unprepared, self-judgment',
                'emotional_tone': 'anxious',
                'category': 'achievement',
                'keywords': 'test, school, unprepared, studying'
            },
            {
                'id': 11,
                'symbol': 'house',
                'meaning': 'Self, psyche, different aspects of personality, security',
                'emotional_tone': 'neutral',
                'category': 'structure',
                'keywords': 'home, building, room, mansion'
            },
            {
                'id': 12,
                'symbol': 'car',
                'meaning': 'Direction in life, control, ambition, journey',
                'emotional_tone': 'neutral',
                'category': 'vehicle',
                'keywords': 'driving, vehicle, automobile, road'
            },
            {
                'id': 13,
                'symbol': 'baby',
                'meaning': 'New beginnings, vulnerability, potential, responsibility',
                'emotional_tone': 'positive',
                'category': 'life',
                'keywords': 'infant, child, newborn, pregnancy'
            },
            {
                'id': 14,
                'symbol': 'cat',
                'meaning': 'Independence, intuition, femininity, mystery',
                'emotional_tone': 'neutral',
                'category': 'animal',
                'keywords': 'kitten, feline, kitty'
            },
            {
                'id': 15,
                'symbol': 'dog',
                'meaning': 'Loyalty, friendship, protection, instinct',
                'emotional_tone': 'positive',
                'category': 'animal',
                'keywords': 'puppy, canine, pet'
            },
            {
                'id': 16,
                'symbol': 'spider',
                'meaning': 'Creativity, feminine energy, feeling trapped, patience',
                'emotional_tone': 'mysterious',
                'category': 'animal',
                'keywords': 'web, arachnid, insect'
            },
            {
                'id': 17,
                'symbol': 'mountain',
                'meaning': 'Challenge, achievement, obstacle, spiritual journey',
                'emotional_tone': 'challenging',
                'category': 'nature',
                'keywords': 'climb, peak, hill, summit'
            },
            {
                'id': 18,
                'symbol': 'bridge',
                'meaning': 'Transition, connection, decision, moving forward',
                'emotional_tone': 'transitional',
                'category': 'structure',
                'keywords': 'crossing, connect, span'
            },
            {
                'id': 19,
                'symbol': 'mirror',
                'meaning': 'Self-reflection, truth, identity, vanity',
                'emotional_tone': 'reflective',
                'category': 'object',
                'keywords': 'reflection, looking glass'
            },
            {
                'id': 20,
                'symbol': 'money',
                'meaning': 'Value, self-worth, power, security, opportunity',
                'emotional_tone': 'neutral',
                'category': 'material',
                'keywords': 'cash, wealth, coins, currency'
            }
        ]
        
        self.data['symbols'] = symbols
        print("✓ Initial dream symbols populated")
    
    def get_next_id(self, collection):
        """Get next available ID for a collection"""
        if not self.data[collection]:
            return 1
        return max(item['id'] for item in self.data[collection]) + 1
    
    def analyze_dream(self, dream_text, save_dream=True):
        """Analyze dream text and find matching symbols"""
        dream_text_lower = dream_text.lower()
        matched_symbols = []
        
        for symbol in self.data['symbols']:
            # Check symbol name
            if symbol['symbol'].lower() in dream_text_lower:
                matched_symbols.append({
                    'symbol': symbol,
                    'relevance': 10
                })
                continue
            
            # Check keywords
            if symbol['keywords']:
                keywords = [kw.strip() for kw in symbol['keywords'].split(',')]
                for keyword in keywords:
                    if keyword.lower() in dream_text_lower:
                        matched_symbols.append({
                            'symbol': symbol,
                            'relevance': 7
                        })
                        break
        
        # Save dream if requested
        dream_id = None
        if save_dream and matched_symbols:
            dream_id = self.save_dream(dream_text)
            if dream_id:
                self.save_interpretations(dream_id, matched_symbols)
        
        return matched_symbols
    
    def save_dream(self, dream_text, mood_before=None, recurring=False):
        """Save user's dream"""
        try:
            dream_id = self.get_next_id('dreams')
            dream = {
                'id': dream_id,
                'dream_text': dream_text,
                'dream_date': datetime.now().strftime('%Y-%m-%d'),
                'mood_before': mood_before,
                'recurring': recurring,
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self.data['dreams'].append(dream)
            self.save_data()
            return dream_id
        except Exception as e:
            print(f"✗ Error saving dream: {e}")
            return None
    
    def save_interpretations(self, dream_id, matched_symbols):
        """Save dream-symbol relationships"""
        try:
            for match in matched_symbols:
                interpretation = {
                    'id': self.get_next_id('interpretations'),
                    'dream_id': dream_id,
                    'symbol_id': match['symbol']['id'],
                    'relevance_score': match['relevance']
                }
                self.data['interpretations'].append(interpretation)
            self.save_data()
        except Exception as e:
            print(f"✗ Error saving interpretations: {e}")
    
    def add_custom_symbol(self, symbol, meaning, emotional_tone, category, keywords):
        """Add new dream symbol"""
        try:
            # Check if symbol already exists
            if any(s['symbol'].lower() == symbol.lower() for s in self.data['symbols']):
                print(f"✗ Symbol '{symbol}' already exists")
                return False
            
            new_symbol = {
                'id': self.get_next_id('symbols'),
                'symbol': symbol,
                'meaning': meaning,
                'emotional_tone': emotional_tone,
                'category': category,
                'keywords': keywords
            }
            self.data['symbols'].append(new_symbol)
            self.save_data()
            print(f"✓ Symbol '{symbol}' added successfully")
            return True
        except Exception as e:
            print(f"✗ Error adding symbol: {e}")
            return False
    
    def get_dream_statistics(self):
        """Get statistics about saved dreams"""
        try:
            total_dreams = len(self.data['dreams'])
            
            # Most common symbols
            symbol_counts = Counter()
            for interp in self.data['interpretations']:
                symbol = next((s for s in self.data['symbols'] if s['id'] == interp['symbol_id']), None)
                if symbol:
                    symbol_counts[symbol['symbol']] += 1
            
            common_symbols = [{'symbol': sym, 'frequency': count} 
                            for sym, count in symbol_counts.most_common(5)]
            
            # Emotional tone distribution
            tone_counts = Counter()
            for interp in self.data['interpretations']:
                symbol = next((s for s in self.data['symbols'] if s['id'] == interp['symbol_id']), None)
                if symbol:
                    tone_counts[symbol['emotional_tone']] += 1
            
            emotional_tones = [{'emotional_tone': tone, 'count': count}
                             for tone, count in tone_counts.items()]
            
            return {
                'total_dreams': total_dreams,
                'common_symbols': common_symbols,
                'emotional_tones': emotional_tones
            }
        except Exception as e:
            print(f"✗ Error getting statistics: {e}")
            return None
    
    def search_dreams_by_symbol(self, symbol_name):
        """Find all dreams containing a specific symbol"""
        try:
            symbol = next((s for s in self.data['symbols'] 
                          if s['symbol'].lower() == symbol_name.lower()), None)
            if not symbol:
                return []
            
            # Find interpretations with this symbol
            dream_ids = [i['dream_id'] for i in self.data['interpretations'] 
                        if i['symbol_id'] == symbol['id']]
            
            # Get dreams
            dreams = [d for d in self.data['dreams'] if d['id'] in dream_ids]
            
            # Add symbol info to each dream
            for dream in dreams:
                dream['symbol'] = symbol['symbol']
                dream['meaning'] = symbol['meaning']
            
            return sorted(dreams, key=lambda x: x['created_at'], reverse=True)
        except Exception as e:
            print(f"✗ Error searching dreams: {e}")
            return []
    
    def display_interpretation(self, matched_symbols):
        """Display dream interpretation results"""
        if not matched_symbols:
            print("\n🌙 No specific symbols found in your dream.")
            print("Try describing your dream with more detail!")
            return
        
        print("\n" + "="*60)
        print("🌙 DREAM INTERPRETATION RESULTS 🌙")
        print("="*60)
        
        for i, match in enumerate(matched_symbols, 1):
            symbol = match['symbol']
            print(f"\n[{i}] Symbol: {symbol['symbol'].upper()}")
            print(f"    Category: {symbol['category']}")
            print(f"    Meaning: {symbol['meaning']}")
            print(f"    Emotional Tone: {symbol['emotional_tone']}")
            print(f"    Relevance: {'★' * (match['relevance'] // 2)}")
        
        print("\n" + "="*60)


def main_menu():
    """Main application menu"""
    print("\n" + "="*60)
    print("✨ WELCOME TO DREAM VISTA ✨")
    print("Your Personal Dream Interpretation Companion")
    print("="*60)
    
    # Initialize app
    app = DreamVista()
    
    while True:
        print("\n📋 MAIN MENU:")
        print("1. Interpret a Dream")
        print("2. Add Custom Symbol")
        print("3. View Dream Statistics")
        print("4. Search Dreams by Symbol")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\n🌙 Describe your dream:")
            dream = input("> ")
            if dream:
                results = app.analyze_dream(dream)
                app.display_interpretation(results)
        
        elif choice == '2':
            print("\n➕ ADD NEW SYMBOL")
            symbol = input("Symbol name: ").strip()
            meaning = input("Meaning: ").strip()
            tone = input("Emotional tone: ").strip()
            category = input("Category: ").strip()
            keywords = input("Keywords (comma-separated): ").strip()
            
            if symbol and meaning:
                app.add_custom_symbol(symbol, meaning, tone, category, keywords)
        
        elif choice == '3':
            print("\n📊 DREAM STATISTICS")
            stats = app.get_dream_statistics()
            if stats:
                print(f"\nTotal Dreams Recorded: {stats['total_dreams']}")
                print("\nMost Common Symbols:")
                for sym in stats['common_symbols']:
                    print(f"  • {sym['symbol']}: {sym['frequency']} times")
                print("\nEmotional Tone Distribution:")
                for tone in stats['emotional_tones']:
                    print(f"  • {tone['emotional_tone']}: {tone['count']}")
        
        elif choice == '4':
            symbol = input("\nEnter symbol to search: ").strip()
            dreams = app.search_dreams_by_symbol(symbol)
            if dreams:
                print(f"\n🔍 Found {len(dreams)} dreams with '{symbol}':")
                for dream in dreams[:5]:  # Show first 5
                    print(f"\n  Date: {dream['dream_date']}")
                    print(f"  Dream: {dream['dream_text'][:100]}...")
            else:
                print(f"No dreams found with symbol '{symbol}'")
        
        elif choice == '5':
            print("\n✨ Sweet dreams! Goodbye! ✨")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()