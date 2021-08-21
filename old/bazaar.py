import requests
import json
import os
import time

# Set styles for print
os.system("")
clear = lambda: os.system('cls')

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BOLD = '\033[01m'
    BG_BLUE = '\033[44m'

item_fetch = requests.get(f'https://api.hypixel.net/skyblock/bazaar?key=9510d4f5-edb3-4fc6-84e7-165d8364b41c')
item_fetch = item_fetch.json()

# Update data in item_fetch
def updateData():
    item_fetch = requests.get(f'https://api.hypixel.net/skyblock/bazaar?key=9510d4f5-edb3-4fc6-84e7-165d8364b41c')
    return item_fetch.json()

# Get buy price of item
def buyPriceOf(item):
    BUY_PRICE = round(item_fetch['products'][item]['sell_summary'][0]['pricePerUnit'], 1)

    return BUY_PRICE

# Get sell price of item
def sellPriceOf(item):
    SELL_PRICE = round(item_fetch['products'][item]['buy_summary'][0]['pricePerUnit'], 1)

    return SELL_PRICE

# Get demand amount
def demandAmount(item):
    SELL_VOLUME = round(item_fetch['products'][item]['quick_status']['buyVolume'], 0)

    return SELL_VOLUME

# Return lowest number in list
def cheapest(list):
    return min(list)

# Return color formatted demand text from amount number
def numberToDemand(number):
    demand = ""
    if demand_number < 10000: demand = f"{style.RED}VERY LOW{style.WHITE}"
    elif demand_number < 100000: demand = f"{style.RED}LOW{style.WHITE}"
    elif demand_number < 250000: demand = f"{style.YELLOW}MEDIUM{style.WHITE}"
    elif demand_number < 500000: demand = f"{style.GREEN}HIGH{style.WHITE}"
    else: demand = f"{style.GREEN}VERY HIGH{style.WHITE}"

    return demand

# Return color foromatted difficulty text from text
def difficultyToFormatted(text):
    difficulty = text
    if text == "VERY EASY" or text == "EASY": difficulty = f"{style.GREEN}{text}{style.WHITE}"
    elif text == "MEDIUM": difficulty = f"{style.YELLOW}MEDIUM{style.WHITE}"
    else: difficulty = f"{style.RED}{text}{style.WHITE}"

    return difficulty


# Set loop to go off every 20 seconds
while (True):
    clear()
    print(f"\t\t\t\t\t\t\t\t\t\tBAZAAR CRAFTABLES\n")
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
                "Fine Jade Gemstone":[ROUGH_JADE_BUY * 80 * 80, FINE_JADE_SELL, 80 * 80, "ROUGH_JADE_GEM", "MEDIUM"],
                "Fine Amber Gemstone":[ROUGH_AMBER_BUY * 80 * 80, FINE_AMBER_SELL, 80 * 80, "ROUGH_AMBER_GEM", "MEDIUM"],
                "Fine Topaz Gemstone":[ROUGH_TOPAZ_BUY * 80 * 80, FINE_TOPAZ_SELL, 80 * 80, "ROUGH_TOPAZ_GEM", "MEDIUM"],
                "Fine Sapphire Gemstone":[ROUGH_SAPPHIRE_BUY * 80 * 80, FINE_SAPPHIRE_SELL, 80 * 80, "ROUGH_SAPPHIRE_GEM", "MEDIUM"],
                "Fine Amethyst Gemstone":[ROUGH_AMETHYST_BUY * 80 * 80, FINE_AMETHYST_SELL, 80 * 80, "ROUGH_AMETHYST_GEM", "MEDIUM"],
                "Fine Jasper Gemstone":[ROUGH_JASPER_BUY * 80 * 80, FINE_JASPER_SELL, 80 * 80, "ROUGH_JASPER_GEM", "MEDIUM"],
                "Fine Ruby Gemstone":[ROUGH_RUBY_BUY * 80 * 80, FINE_RUBY_SELL, 80 * 80, "ROUGH_RUBY_GEM", "MEDIUM"]
            }

    sorted_list = []
    item_list = []
    for key in crafts:
        profit = round((1728 / crafts[key][2]) * (crafts[key][1] - crafts[key][0]), 0)

        loops = 0
        added = False
        for i in sorted_list:
            if profit > i:
                sorted_list.insert(loops, profit)
                item_list.insert(loops, key)
                added = True
                break
            loops += 1

        if not added:
            sorted_list.insert(len(sorted_list), profit)
            item_list.insert(len(item_list), key)

    colored = True
    for key in item_list:
        try:
            colored = not colored

            buy_price = f"{round(crafts[key][0], 0):<8} buy price"
            sell_price = f"{round(crafts[key][1], 0):<8} sell price"
            demand_number = demandAmount(crafts[key][3])
            demand = f"{numberToDemand(demand_number):<19} Demand"
            difficulty = difficultyToFormatted(crafts[key][4])

            if crafts[key][1] == crafts[key][0] or (round((1728 / crafts[key][2]) * (crafts[key][1] - crafts[key][0]), 0) - 1000 <= 0 and crafts[key][1] > crafts[key][0]) or (round((1728 / crafts[key][2]) * (crafts[key][1] - crafts[key][0]), 0) > -100 and round((1728 / crafts[key][2]) * (crafts[key][1] - crafts[key][0]), 0) < 0):
                color = style.YELLOW
            elif (crafts[key][1] - crafts[key][0]) > 0:
                color = style.GREEN
            else:
                color = style.RED

            profit_inventory = f"{color}{int((1728 / crafts[key][2]) * (crafts[key][1] - crafts[key][0])):<7}{style.WHITE}"
            if not "-" in profit_inventory: profit_inventory = " " + profit_inventory
            else: profit_inventory = profit_inventory + " "
            profit_inventory += "profit per inventory"

            profit = f"{color}{round(crafts[key][1] - crafts[key][0], 0):<9}{style.WHITE}"
            if not "-" in profit: profit = " " + profit
            else: profit = profit + " "
            profit +=  f"profit per item ({color}{round((crafts[key][1] / crafts[key][0] - 1) * 100, 0):<6}%{style.WHITE})"

            if colored:
                print(f'{style.BG_BLUE}{key:<23} | {buy_price} | {sell_price} | {profit} | {profit_inventory} | {demand} | {difficulty:<19} Difficulty{style.RESET}')
            else:
                print(f'{key:<23} | {buy_price} | {sell_price} | {profit} | {profit_inventory} | {demand} | {difficulty:<19} Difficulty')
        except Exception as e:
            pass

    i = 30
    while (i > 0):
        time.sleep(1)
        i -= 1
        print(f" {i} sec until next update", end='\r')
    updateData()
