from collections import UserList
from deta import Deta

deta = Deta()

class Database:
    def __init__(self):
        self.guilds = deta.Base("guilds")
        self.users = deta.Base("users")
        
    # ========== GUILD METHODS ==========

    def get_guild(self, guild_id):
        return self.guilds.get(guild_id)

    def create_guild(self, guild_id, guild_name)
        self.guilds.put({
            "key": guild_id,
            "name": guild_name,
            "words": []
        })
    
    def delete_guild(self, guild_id):
        self.guilds.delete(guild_id)
    
    # ========== USER METHODS ==========
    
    def get_user(self, user_id):
        return self.users.get(user_id)

    def create_user(self, guild_id, member_id, member_name):
        new_user = {
            "guild_id": guild_id,
            "member_id": member_id,
            "member_name": member_name,
        }
        words = self.get_words(guild_id)
        new_user["words"] = words
        self.users.put(new_user)
    
    def delete_user(self, user_id):
        self.users.delete(user_id)

    def __update_all_users_in_guild(self, update_dict, guild_id):
        users = self.users.fetch({"guild_id": guild_id})
        for user in users:
            self.users.update(update_dict, user["key"])

    # ========== WORD METHODS ==========

    def get_words(self, guild_id):
        return self.guilds.get(guild_id)["words"]

    def add_word(self, guild_id, word, stem):
        word_dict = {
            "word": word,
            "stem": stem,
            "count": 0
        }
        self.guilds.update({
            "words": self.guilds.util.append(word_dict)
        }, guild_id)
        self.__update_all_users_in_guild({
            "words": self.users.util.append(word_dict)
        }, guild_id)

    def increment_word(self, guild_id, member_id, word, count):
        user = self.users.fetch({"guild_id": guild_id, "member_id": member_id})
        if user:
            for word in user["words"]:
                if word["word"] == word:
                    word["count"] += count
                    self.users.update({
                        "words": user["words"]
                    }, user["key"])
                    break
