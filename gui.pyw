##
#   TODO: Image to crafts
#   TODO: Image recipy
#   TODO: Show what column is being sorted after
##

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
    try:
        BUY_PRICE = round(item_fetch['products'][item]['sell_summary'][0]['pricePerUnit'], 1)
    except:
        BUY_PRICE = 0

    return BUY_PRICE + 0.1

# Get sell price of item
def sellPriceOf(item):
    try:
        SELL_PRICE = round(item_fetch['products'][item]['buy_summary'][0]['pricePerUnit'], 1)
    except:
        SELL_PRICE = 0.1

    return SELL_PRICE - 0.1

# Get demand amount
def demandAmount(item):
    SELL_VOLUME = round(item_fetch['products'][item]['quick_status']['buyVolume'], 0)

    return SELL_VOLUME

def updateData():
    global item_fetch
    item_fetch = requests.get(f'https://api.hypixel.net/skyblock/bazaar?key=9510d4f5-edb3-4fc6-84e7-165d8364b41c')
    item_fetch = item_fetch.json()

    return item_fetch

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
    item_fetch = updateData()

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

    IRON_BUY = buyPriceOf("IRON_INGOT")
    GOLD_BUY = buyPriceOf("GOLD_INGOT")
    DIAMOND_BUY = buyPriceOf("DIAMOND")
    COBBLESTONE_BUY = buyPriceOf("COBBLESTONE")
    COAL_BUY = buyPriceOf("COAL")
    EMERALD_BUY = buyPriceOf("EMERALD")
    REDSTONE_BUY = buyPriceOf("REDSTONE")
    QUARTZ_BUY = buyPriceOf("QUARTZ")
    OBSIDIAN_BUY = buyPriceOf("OBSIDIAN")
    GLOWSTONE_BUY = buyPriceOf("GLOWSTONE_DUST")
    HARD_STONE_BUY = buyPriceOf("HARD_STONE")
    ICE_BUY = buyPriceOf("ICE")
    SAND_BUY = buyPriceOf("SAND")
    MITHRIL_BUY = buyPriceOf("MITHRIL_ORE")
    TITANIUM_BUY = buyPriceOf("TITANIUM_ORE")

    ROTTEN_FLESH_BUY = buyPriceOf("ROTTEN_FLESH")
    BONE_BUY = buyPriceOf("BONE")
    STRING_BUY = buyPriceOf("STRING")
    SPIDER_EYE_BUY = buyPriceOf("SPIDER_EYE")
    GUNPOWDER_BUY = buyPriceOf("GUNPOWDER")
    ENDER_PEARL_BUY = buyPriceOf("ENDER_PEARL")
    SLIME_BALL_BUY = buyPriceOf("SLIME_BALL")
    BLAZE_ROD_BUY = buyPriceOf("BLAZE_ROD")

    # {"ITEM-NAME: [PRICE_CALULATION, TOTAL ITEMS PER CRAFT, ITEM NAME API, CRAFTING DIFFICULTY, FORGE REQUIRED, BITS REQUIRED]"}
    crafts = {
        "Enchanted Charcoal":[cheapest([OAK_BUY, SPRUCE_OAK_BUY, BIRCH_OAK_BUY, JUNGLE_OAK_BUY, DARK_OAK_BUY, ACACIA_OAK_BUY]) * 32 + COAL_BUY * 128, 160, "ENCHANTED_CHARCOAL", "EASY", False, False],
        "Snow Block":[SNOW_BALL_BUY * 2, 4, "SNOW_BLOCK", "VERY EASY", False, False],
        "Fish Bait":[RAW_FISH_BUY * 2 + SALMON_BUY, 3, "FISH_BAIT", "EASY", False, False],
        "Light Bait":[RAW_FISH_BUY + PRISMARINE_CRYSTALS_BUY * 2, 3, "LIGHT_BAIT", "EASY", False, False],
        "Dark Bait":[RAW_FISH_BUY + INK_SACK_BUY, 2, "DARK_BAIT", "EASY", False, False],
        "Spiked Bait":[RAW_FISH_BUY + PUFFERFISH_BUY, 2, "SPIKED_BAIT", "EASY", False, False],
        "Spooky Bait":[RAW_FISH_BUY + PUMPKIN_BUY, 2, "SPOOKY_BAIT", "EASY", False, False],
        "Carrot Bait":[RAW_FISH_BUY + CARROT_BUY, 2, "CARROT_BAIT", "EASY", False, False],
        "Blessed Bait":[RAW_FISH_BUY + GOLD_BLOCK_BUY + PRISMARINE_CRYSTALS_BUY, 3, "BLESSED_BAIT", "MEDIUM", False, False],
        "Whale Bait":[FISH_BAIT_BUY + LIGHT_BAIT_BUY + DARK_BAIT_BUY + BLESSED_BAIT_BUY, 4, "WHALE_BAIT", "HARD", False, False],
        "Ice Bait":[RAW_FISH_BUY + ICE_BUY, 2, "ICE_BAIT", "EASY", False, False],
        "Enchanted Rabbit Foot":[RABBIT_FOOT_BUY * 160, 160, "ENCHANTED_RABBIT_FOOT", "EASY", False, False],
        "Fine Jade Gemstone":[ROUGH_JADE_BUY * 80 * 80, 80 * 80, "FINE_JADE_GEM", "MEDIUM", False, False],
        "Fine Amber Gemstone":[ROUGH_AMBER_BUY * 80 * 80, 80 * 80, "FINE_AMBER_GEM", "MEDIUM", False, False],
        "Fine Topaz Gemstone":[ROUGH_TOPAZ_BUY * 80 * 80, 80 * 80, "FINE_TOPAZ_GEM", "MEDIUM", False, False],
        "Fine Sapphire Gemstone":[ROUGH_SAPPHIRE_BUY * 80 * 80, 80 * 80, "FINE_SAPPHIRE_GEM", "MEDIUM", False, False],
        "Fine Amethyst Gemstone":[ROUGH_AMETHYST_BUY * 80 * 80, 80 * 80, "FINE_AMETHYST_GEM", "MEDIUM", False, False],
        "Fine Jasper Gemstone":[ROUGH_JASPER_BUY * 80 * 80, 80 * 80, "FINE_JASPER_GEM", "MEDIUM", False, False],
        "Fine Ruby Gemstone":[ROUGH_RUBY_BUY * 80 * 80, 80 * 80, "FINE_RUBY_GEM", "MEDIUM", False, False],
        "Enchanted Hard Stone":[HARD_STONE_BUY * 64 * 9, 64 * 9, "ENCHANTED_HARD_STONE", "MEDIUM", False, False],
        "Enchanted Iron":[IRON_BUY * 160, 160, "ENCHANTED_IRON", "EASY", False, False],
        "Enchanted Gold":[GOLD_BUY * 160, 160, "ENCHANTED_GOLD", "EASY", False, False],
        "Enchanted Diamond":[DIAMOND_BUY * 160, 160, "ENCHANTED_DIAMOND", "EASY", False, False],
        "Enchanted Cobblestone":[COBBLESTONE_BUY * 160, 160, "ENCHANTED_COBBLESTONE", "EASY", False, False],
        "Enchanted Coal":[COAL_BUY * 160, 160, "ENCHANTED_COAL", "EASY", False, False],
        "Enchanted Emerald":[EMERALD_BUY * 160, 160, "ENCHANTED_EMERALD", "EASY", False, False],
        "Enchanted Redstone":[REDSTONE_BUY * 160, 160, "ENCHANTED_REDSTONE", "EASY", False, False],
        "Enchanted Quartz":[QUARTZ_BUY * 160, 160, "ENCHANTED_QUARTZ", "EASY", False, False],
        "Enchanted Obsidian":[OBSIDIAN_BUY * 160, 160, "ENCHANTED_OBSIDIAN", "EASY", False, False],
        "Enchanted Glowstone Dust":[GLOWSTONE_BUY * 160, 160, "ENCHANTED_GLOWSTONE_DUST", "EASY", False, False],
        "Enchanted Hard Stone":[HARD_STONE_BUY * 64 * 9, 64 * 9, "ENCHANTED_HARD_STONE", "MEDIUM", False, False],
        "Enchanted Ice":[ICE_BUY * 160, 160, "ENCHANTED_ICE", "EASY", False, False],
        "Enchanted Sand":[SAND_BUY * 160, 160, "ENCHANTED_SAND", "EASY", False, False],
        "Enchanted Mithril":[MITHRIL_BUY * 160, 160, "ENCHANTED_MITHRIL", "MEDIUM", False, False],
        "Refined Mithril":[MITHRIL_BUY * 160 * 160, 160 * 160, "REFINED_MITHRIL", "HARD", True, False],
        "Enchanted Titanium":[TITANIUM_BUY * 160, 160, "ENCHANTED_TITANIUM", "MEDIUM", False, False],
        "Refined Titanium":[TITANIUM_BUY * 160 * 16, 160 * 16, "REFINED_TITANIUM", "HARD", True, False],
        "Enchanted Rotten Flesh":[ROTTEN_FLESH_BUY * 160, 160, "ENCHANTED_ROTTEN_FLESH", "EASY", False, False],
        "Enchanted Bone":[BONE_BUY * 160, 160, "ENCHANTED_BONE", "Easy", False, False],
        "Enchanted String":[STRING_BUY * 160, 160, "ENCHANTED_STRING", "Easy", False, False],
        "Enchanted Spider Eye":[SPIDER_EYE_BUY * 160, 160, "ENCHANTED_SPIDER_EYE", "Easy", False, False],
        "Enchanted Gunpowder":[GUNPOWDER_BUY * 160, 160, "ENCHANTED_GUNPOWDER", "Easy", False, False],
        "Enchanted Enderpearl":[ENDER_PEARL_BUY * 20, 20, "ENCHANTED_ENDER_PEARL", "Easy", False, False],
        "Enchanted Slime":[SLIME_BALL_BUY * 160, 160, "ENCHANTED_SLIME_BALL", "Easy", False, False],
        "Enchanted Slime Block":[SLIME_BALL_BUY * 160 * 160, 160 * 160, "ENCHANTED_SLIME_BLOCK", "Medium", False, False],
        "Enchanted Blaze Powder":[BLAZE_ROD_BUY * 160, 160, "ENCHANTED_BLAZE_POWDER", "Easy", False, False],
        "Enchanted Blaze Rod":[BLAZE_ROD_BUY * 160 * 160, 160 * 160, "ENCHANTED_BLAZE_ROD", "Medium", False, False],
        "Enchanted Lava Bucket":[COAL_BUY * 160 * 160 * 2 + IRON_BUY * 160 * 3, 160 * 5, "ENCHANTED_LAVA_BUCKET", "Hard", False, False],
        "Magma Bucket (w.o Heat Core)":[COAL_BUY * 160 * 160 * 2 * 2 + IRON_BUY * 160 * 3 * 2, 160 * 5 * 2, "MAGMA_BUCKET", "Very Hard", False, True],
        "Enchanted Oak":[OAK_BUY * 160, 160, "ENCHANTED_OAK_LOG", "Easy", False, False],
        "Enchanted Spruce":[SPRUCE_OAK_BUY * 160, 160, "ENCHANTED_SPRUCE_LOG", "Easy", False, False],
        "Enchanted Birch":[BIRCH_OAK_BUY * 160, 160, "ENCHANTED_BIRCH_LOG", "Easy", False, False],
        "Enchanted Dark Oak":[DARK_OAK_BUY * 160, 160, "ENCHANTED_DARK_OAK_LOG", "Easy", False, False],
        "Enchanted Acacia":[ACACIA_OAK_BUY * 160, 160, "ENCHANTED_ACACIA_LOG", "Easy", False, False],
        "Enchanted Jungle":[JUNGLE_OAK_BUY * 160, 160, "ENCHANTED_JUNGLE_LOG", "Easy", False, False]
    }

    result = {}

    for key in crafts:
        # Buyprice
        buyprice = round(crafts[key][0], 1)

        # Sellprice
        sellprice = round(sellPriceOf(crafts[key][2]), 1)

        # Profit per item
        profit_per_item = round(sellprice - buyprice, 1)

        # Profit per item in percentage
        profit_per_item_percentage = round((sellprice / buyprice - 1) * 100, 1)

        # Profit per inventory
        profit_inventory = int((1728 / crafts[key][1]) * (sellprice - buyprice))

        # Demand
        demand = demandAmount(crafts[key][2])

        # Difficulty
        difficulty = difficultyToFormatted(crafts[key][3])

        # Forge Required
        forge_needed = crafts[key][4]

        # Forge Required
        bits_needed = crafts[key][5]

        result[key] = [buyprice, sellprice, profit_per_item, profit_per_item_percentage, profit_inventory, demand, difficulty, forge_needed, bits_needed] # Add to resultlist

    return result # Return the dictionary with the result

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.CreateUI()
        self.LoadTable()

        # Set the order
        self.order_after = 0

        # Button for disabling view of items you lose on
            # Loss
        self.show_loss = IntVar()
        self.cb1 = Checkbutton(self, text = "Show Loss", variable = self.show_loss, onvalue = 1, offvalue = 0, command = self.clicked_checkbox)
        self.cb1.grid()
        self.show_loss.set(1)
            # Forge
        self.show_forge = IntVar()
        self.cb2 = Checkbutton(self, text = "Show Forge", variable = self.show_forge, onvalue = 1, offvalue = 0, command = self.clicked_checkbox)
        self.cb2.grid()
        self.show_forge.set(1)
            # Show Items Bought by Bits
        self.show_bits = IntVar()
        self.cb3 = Checkbutton(self, text = "Show Items Needing Bits", variable = self.show_bits, onvalue = 1, offvalue = 0, command = self.clicked_checkbox)
        self.cb3.grid()
        self.show_bits.set(0)
        #     # Selector
        # Label(self, text = "Minimum Demand :", font = ("Times New Roman", 10)).grid(row = 0, column = 4)
        # show_minimum = StringVar()
        # chosen = Combobox(self, width = 27, textvariable = show_minimum)
        # chosen['values'] = ('NO MINIMUM', 'LOW', 'MEDIUM', 'HIGH', 'VERY HIGH')
        # chosen.grid(row = 0, column = 5)
        # show_minimum.set('NO MINIMUM')

        self.grid(sticky = (N, S, W, E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        self.updater()

    def CreateUI(self):
        tv = Treeview(self)

        # Scrollbar
        vsb = Scrollbar(self, orient="vertical", command=tv.yview)
        vsb.place(relx=0.978, rely=0.0, relheight=0.9, relwidth=0.020)
        tv.configure(yscrollcommand=vsb.set)

        tv.heading("#0", text='Item', anchor='center')
        tv.column("#0", anchor="center")
        tv['columns'] = ('Buyprice', 'Sellprice', 'Profit per item', 'Profit per item %', 'Profit per inventory', 'Demand', 'Forge Required')
        for header in tv['columns']:
            tv.heading(header, text=header)
            tv.column(header, anchor="center", width=100)
        tv.grid(sticky = (N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        tv.bind("<Double-1>", self.on_double_click) # Event for click to sort by row

    def LoadTable(self):
        self.item_list = getUpdatedData()
        for item in self.item_list:
            self.treeview.insert('', 'end', text=item, values=(f"${self.item_list[item][0]}", f"${self.item_list[item][1]}", f"${self.item_list[item][2]}", f"{self.item_list[item][3]}%", f"${self.item_list[item][4]}", f"{numberToDemand(self.item_list[item][5])} Demand", self.item_list[item][7]))

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

        self.item_list = getUpdatedData()

        order_by = self.order_by(self.order_after)

        # Insert new and sorted ones
        for id in order_by:
            for item in self.item_list:
                if item == id:
                    # Don't add the item if the user does not want to have it displayed
                    if self.show_loss.get() == 0 and self.item_list[item][2] < 0:
                        break
                    if self.show_forge.get() == 0 and self.item_list[item][7] == True:
                        break
                    if self.show_bits.get() == 0 and self.item_list[item][8] == True:
                        break

                    self.treeview.insert('', 'end', text=item, values=(f"${self.item_list[item][0]}", f"${self.item_list[item][1]}", f"${self.item_list[item][2]}", f"{self.item_list[item][3]}%", f"${self.item_list[item][4]}", f"{numberToDemand(self.item_list[item][5])} Demand", self.item_list[item][7]))
                    break

    def update_data(self):
        self.item_list = getUpdatedData()
        self.clear_and_populate()

    def clicked_checkbox(self):
        self.clear_and_populate()

    def updater(self):
        self.after(30000, self.updater)
        self.after(30000, self.update_data)

def main():
    gui = Tk()
    gui.geometry("1200x475")
    gui.title("SkyBlock - Bazaar Craftables")
    gui.iconbitmap('favicon.ico')
    app = App(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()
