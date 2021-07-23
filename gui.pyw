try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *

# Import Requests and json
import requests
import json
import os
from time import sleep

# Initial fetch of data
item_fetch = requests.get(f'https://api.hypixel.net/skyblock/bazaar?key=9510d4f5-edb3-4fc6-84e7-165d8364b41c')
item_fetch = item_fetch.json()

# Get buy price of item
def buyPriceOf(item):
    BUY_PRICE = round(item_fetch['products'][item]['sell_summary'][0]['pricePerUnit'], 1)
    return BUY_PRICE + 0.1

# Get sell price of item
def sellPriceOf(item):
    SELL_PRICE = round(item_fetch['products'][item]['buy_summary'][0]['pricePerUnit'], 1)
    return SELL_PRICE - 0.1

# Get demand amount
def demandAmount(item):
    SELL_VOLUME = round(item_fetch['products'][item]['quick_status']['buyVolume'], 0)
    return SELL_VOLUME

def updateData():
    item_fetch = requests.get(f'https://api.hypixel.net/skyblock/bazaar?key=9510d4f5-edb3-4fc6-84e7-165d8364b41c')
    item_fetch = item_fetch.json()

# Return color formatted demand text from amount number
def numberToDemand(demand_number):
    demand = ""
    if demand_number < 10000: demand = f"VERY LOW"
    elif demand_number < 100000: demand = f"LOW"
    elif demand_number < 250000: demand = f"MEDIUM"
    elif demand_number < 500000: demand = f"HIGH"
    else: demand = f"VERY HIGH"

    return demand

# Return color foromatted difficulty text from text
def difficultyToFormatted(text):
    difficulty = text
    if text == "VERY EASY" or text == "EASY": difficulty = f"{text}"
    elif text == "MEDIUM": difficulty = f"MEDIUM"
    else: difficulty = f"{text}"

    return difficulty

# Return lowest number in list
def cheapest(list):
    return min(list)

######################
# FETCH UPDATED DATA #
######################
def getUpdatedData():
    updateData()

    # BUY PRICES
    RAW_FISH_BUY = buyPriceOf("RAW_FISH")
    SALMON_BUY = buyPriceOf("RAW_FISH:1")
    COAL_BUY = buyPriceOf("COAL")
    OAK_BUY = buyPriceOf("LOG")
    SPRUCE_OAK_BUY = buyPriceOf("LOG:1")
    BIRCH_OAK_BUY = buyPriceOf("LOG:2")
    JUNGLE_OAK_BUY = buyPriceOf("LOG:3")
    DARK_OAK_BUY = buyPriceOf("LOG_2:1")
    ACACIA_OAK_BUY = buyPriceOf("LOG_2")
    SNOW_BALL_BUY = buyPriceOf("SNOW_BALL")
    SAND_BUY = buyPriceOf("SAND")
    PRISMARINE_CRYSTALS_BUY = buyPriceOf("PRISMARINE_CRYSTALS")
    INK_SACK_BUY = buyPriceOf("INK_SACK")
    PUFFERFISH_BUY = buyPriceOf("RAW_FISH:3")
    PUMPKIN_BUY = buyPriceOf("PUMPKIN")
    CARROT_BUY = buyPriceOf("CARROT_ITEM")
    GOLD_BLOCK_BUY = buyPriceOf("GOLD_INGOT") * 9
    ICE_BUY = buyPriceOf("ICE")
    SHARK_FIN_BUY = buyPriceOf("SHARK_FIN")
    FISH_BAIT_BUY = buyPriceOf("FISH_BAIT")
    LIGHT_BAIT_BUY = buyPriceOf("LIGHT_BAIT")
    DARK_BAIT_BUY = buyPriceOf("DARK_BAIT")
    BLESSED_BAIT_BUY = buyPriceOf("BLESSED_BAIT")
    RABBIT_FOOT_BUY = buyPriceOf("RABBIT_FOOT")

    ROUGH_JADE_BUY = buyPriceOf("ROUGH_JADE_GEM")
    ROUGH_AMBER_BUY = buyPriceOf("ROUGH_AMBER_GEM")
    ROUGH_TOPAZ_BUY = buyPriceOf("ROUGH_TOPAZ_GEM")
    ROUGH_SAPPHIRE_BUY = buyPriceOf("ROUGH_SAPPHIRE_GEM")
    ROUGH_AMETHYST_BUY = buyPriceOf("ROUGH_AMETHYST_GEM")
    ROUGH_JASPER_BUY = buyPriceOf("ROUGH_JASPER_GEM")
    ROUGH_RUBY_BUY = buyPriceOf("ROUGH_RUBY_GEM")
    HARD_STONE_BUY = buyPriceOf("HARD_STONE")

    # SELL PRICES
    FISH_BAIT_SELL = sellPriceOf("FISH_BAIT")
    ENCHANTED_CHARCOAL_SELL = sellPriceOf("ENCHANTED_CHARCOAL")
    SNOW_BLOCK_SELL = sellPriceOf("SNOW_BLOCK")
    ENCHANTED_SAND_SELL = sellPriceOf("ENCHANTED_SAND")
    MINNOW_BAIT_SELL = sellPriceOf("MINNOW_BAIT")
    LIGHT_BAIT_SELL = sellPriceOf("LIGHT_BAIT")
    DARK_BAIT_SELL = sellPriceOf("DARK_BAIT")
    SPIKED_BAIT_SELL = sellPriceOf("SPIKED_BAIT")
    SPOOKY_BAIT_SELL = sellPriceOf("SPOOKY_BAIT")
    CARROT_BAIT_SELL = sellPriceOf("CARROT_BAIT")
    BLESSED_BAIT_SELL = sellPriceOf("BLESSED_BAIT")
    WHALE_BAIT_SELL = sellPriceOf("WHALE_BAIT")
    ICE_BAIT_SELL = sellPriceOf("ICE_BAIT")
    SHARK_BAIT_SELL = sellPriceOf("SHARK_BAIT")
    ENCHANTED_RABBIT_FOOT_SELL = sellPriceOf("ENCHANTED_RABBIT_FOOT")

    FINE_JADE_SELL = sellPriceOf("FINE_JADE_GEM")
    FINE_AMBER_SELL = sellPriceOf("FINE_AMBER_GEM")
    FINE_TOPAZ_SELL = sellPriceOf("FINE_TOPAZ_GEM")
    FINE_SAPPHIRE_SELL = sellPriceOf("FINE_SAPPHIRE_GEM")
    FINE_AMETHYST_SELL = sellPriceOf("FINE_AMETHYST_GEM")
    FINE_JASPER_SELL = sellPriceOf("FINE_JASPER_GEM")
    FINE_RUBY_SELL = sellPriceOf("FINE_RUBY_GEM")
    ENCHANTED_HARD_STONE_SELL = sellPriceOf("ENCHANTED_HARD_STONE")

    # {"ITEM-NAME: [PRICE_CALULATION, SELL_CALCULATION, TOTAL ITEMS PER CRAFT, ITEM NAME API, CRAFTING DIFFICULTY]"}
    crafts = {
        "Enchanted Charcoal":[cheapest([OAK_BUY, SPRUCE_OAK_BUY, BIRCH_OAK_BUY, JUNGLE_OAK_BUY, DARK_OAK_BUY, ACACIA_OAK_BUY]) * 32 + COAL_BUY * 128, ENCHANTED_CHARCOAL_SELL, 160, "ENCHANTED_CHARCOAL", "EASY"],
        "Snow Block":[SNOW_BALL_BUY * 2, SNOW_BLOCK_SELL, 4, "SNOW_BLOCK", "VERY EASY"],
        "Fish Bait":[RAW_FISH_BUY * 2 + SALMON_BUY, FISH_BAIT_SELL, 3, "FISH_BAIT", "EASY"],
        "Light Bait":[RAW_FISH_BUY + PRISMARINE_CRYSTALS_BUY * 2, LIGHT_BAIT_SELL, 3, "LIGHT_BAIT", "EASY"],
        "Dark Bait":[RAW_FISH_BUY + INK_SACK_BUY, DARK_BAIT_SELL, 2, "DARK_BAIT", "EASY"],
        "Spiked Bait":[RAW_FISH_BUY + PUFFERFISH_BUY, SPIKED_BAIT_SELL, 2, "SPIKED_BAIT", "EASY"],
        "Spooky Bait":[RAW_FISH_BUY + PUMPKIN_BUY, SPOOKY_BAIT_SELL, 2, "SPOOKY_BAIT", "EASY"],
        "Carrot Bait":[RAW_FISH_BUY + CARROT_BUY, CARROT_BAIT_SELL, 2, "CARROT_BAIT", "EASY"],
        "Blessed Bait":[RAW_FISH_BUY + GOLD_BLOCK_BUY + PRISMARINE_CRYSTALS_BUY, BLESSED_BAIT_SELL, 3, "BLESSED_BAIT", "MEDIUM"],
        "Whale Bait":[FISH_BAIT_BUY + LIGHT_BAIT_BUY + DARK_BAIT_BUY + BLESSED_BAIT_BUY, WHALE_BAIT_SELL, 4, "WHALE_BAIT", "HARD"],
        "Ice Bait":[RAW_FISH_BUY + ICE_BUY, ICE_BAIT_SELL, 2, "ICE_BAIT", "EASY"],
        "Enchanted Rabbit Foot":[RABBIT_FOOT_BUY * 160, ENCHANTED_RABBIT_FOOT_SELL, 160, "ENCHANTED_RABBIT_FOOT", "EASY"],
        "Fine Jade Gemstone":[ROUGH_JADE_BUY * 80 * 80, FINE_JADE_SELL, 80 * 80, "FINE_JADE_GEM", "MEDIUM"],
        "Fine Amber Gemstone":[ROUGH_AMBER_BUY * 80 * 80, FINE_AMBER_SELL, 80 * 80, "FINE_AMBER_GEM", "MEDIUM"],
        "Fine Topaz Gemstone":[ROUGH_TOPAZ_BUY * 80 * 80, FINE_TOPAZ_SELL, 80 * 80, "FINE_TOPAZ_GEM", "MEDIUM"],
        "Fine Sapphire Gemstone":[ROUGH_SAPPHIRE_BUY * 80 * 80, FINE_SAPPHIRE_SELL, 80 * 80, "FINE_SAPPHIRE_GEM", "MEDIUM"],
        "Fine Amethyst Gemstone":[ROUGH_AMETHYST_BUY * 80 * 80, FINE_AMETHYST_SELL, 80 * 80, "FINE_AMETHYST_GEM", "MEDIUM"],
        "Fine Jasper Gemstone":[ROUGH_JASPER_BUY * 80 * 80, FINE_JASPER_SELL, 80 * 80, "FINE_JASPER_GEM", "MEDIUM"],
        "Fine Ruby Gemstone":[ROUGH_RUBY_BUY * 80 * 80, FINE_RUBY_SELL, 80 * 80, "FINE_RUBY_GEM", "MEDIUM"],
        "Enchanted Hard Stone":[HARD_STONE_BUY * 64 * 9, ENCHANTED_HARD_STONE_SELL, 64 * 9, "ENCHANTED_HARD_STONE", "MEDIUM"]
    }

    result = {}

    for key in crafts:
        # Buyprice
        buyprice = round(crafts[key][0], 1)

        # Sellprice
        sellprice = round(crafts[key][1], 1)

        # Profit per item
        profit_per_item = round(sellprice - buyprice, 1)

        # Profit per item in percentage
        profit_per_item_percentage = round((crafts[key][1] / crafts[key][0] - 1) * 100, 1)

        # Profit per inventory
        profit_inventory = int((1728 / crafts[key][2]) * (crafts[key][1] - crafts[key][0]))

        # Demand
        demand = demandAmount(crafts[key][3])

        # Difficulty
        difficulty = difficultyToFormatted(crafts[key][4])

        result[key] = [buyprice, sellprice, profit_per_item, profit_per_item_percentage, profit_inventory, demand, difficulty] # Add to resultlist

    return result # Return the dictionary with the result

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N, S, W, E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        self.updater()

    def CreateUI(self):
        tv = Treeview(self)
        tv.heading("#0", text='Item', anchor='center')
        tv.column("#0", anchor="center")
        tv['columns'] = ('Buyprice', 'Sellprice', 'Profit per item', 'Profit per item %', 'Profit per inventory', 'Demand')
        for header in tv['columns']:
            tv.heading(header, text=header)
            tv.column(header, anchor="center", width=100)
        tv.grid(sticky = (N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        tv.bind("<Double-1>", self.on_double_click)

    def LoadTable(self):
        self.item_list = getUpdatedData()
        for item in self.item_list:
            self.treeview.insert('', 'end', text=item, values=(f"${self.item_list[item][0]}", f"${self.item_list[item][1]}", f"${self.item_list[item][2]}", f"{self.item_list[item][3]}%", f"${self.item_list[item][4]}", f"{numberToDemand(self.item_list[item][5])} Demand"))

    def order_by(self, index):
        ordered_list = []
        ordered_values = []

        if index >= 0 and index < 6:
            loopsx = 0
            for item in self.item_list:
                loopsy = 0
                for number in ordered_values:
                    if self.item_list[item][index] >= number:
                        ordered_list.insert(loopsy, item)
                        ordered_values.insert(loopsy, self.item_list[item][index])
                        break
                    loopsy += 1
                loopsx += 1

                if loopsx > len(ordered_list):
                    ordered_list.append(item)
                    ordered_values.append(self.item_list[item][index])
        elif index == -1:
            ordered_list = list(self.item_list.keys())
            ordered_list.sort()

        return ordered_list

    def on_double_click(self, event):
        region = self.treeview.identify("region", event.x, event.y)
        column = self.treeview.identify("column", event.x, event.y)
        if region == "heading":
            self.clear_and_populate(column)

    def clear_and_populate(self, column=None):
        # Delete all previous values from the table
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        if column != None:
            # Order list after the given column
            self.order_after = int(column.replace('#', '')) - 1

        order_by = self.order_by(self.order_after)

        # Insert new and sorted ones
        for id in order_by:
            for item in self.item_list:
                if item == id:
                    self.treeview.insert('', 'end', text=item, values=(f"${self.item_list[item][0]}", f"${self.item_list[item][1]}", f"${self.item_list[item][2]}", f"{self.item_list[item][3]}%", f"${self.item_list[item][4]}", f"{numberToDemand(self.item_list[item][5])} Demand"))
                    break

    def update_data(self):
        self.item_list = getUpdatedData()
        self.clear_and_populate()

    def updater(self):
        self.after(15000, self.updater)
        self.after(15000, self.update_data)

def main():
    gui = Tk()
    gui.geometry("1200x475")
    gui.title("SkyBlock - Bazaar Craftables")
    gui.iconbitmap('favicon.ico')
    app = App(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()
