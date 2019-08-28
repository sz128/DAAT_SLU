# -*- coding: utf-8 -*-

dstc2_templates = {

    'ack': ['okay', 'ok'],
    'hello': ['hello'],
    'affirm': ['yes'],
    'bye': ['goodbye', 'good bye', 'bye'],
    'negate': ['no'],
    'repeat': ['repeat that'],
    'reqalts': ['how about', 'what about', 'anything else', 'what else'],
    'reqmore': ['more'],
    'restart': ['start over'],
    'thankyou': ['thank you'],

    'request-food': ['type of food', 'what kind of food do they serve'],
    'request-addr': ['the address', 'whats the address', 'can i get the address'],
    'request-area': ['the area', 'what area'],
    'request-name': ['what is the name', 'the name'],
    'request-phone': ['what is the phone number', 'the phone number'],
    'request-postcode': ['post code', 'the postcode'],
    'request-pricerange': ['the price range', 'can i get the price range'],
    'request-signature': ['the signature'],

    'inform-food-[food]': ['[food]', '[food] food', 'serve [food] food'],
    'confirm-food-[food]': ['does it serve [food] food', 'is it [food]'],
    'deny-food-[food]': ['i dont want [food]', 'not [food] food'],

    'inform-name-[name]': ['[name]'],
    'confirm-name-[name]': ['is it [name]'],
    'deny-name-[name]': ['not [name]', 'hate [name]', 'fuck [name]'],

    'inform-area-[area]': ['in the [area] part of town', '[area]', 'in the [area]'],
    'confirm-area-[area]': ['is it in the [area] of town'],
    'deny-area-[area]': ['not in the [area]'],

    'inform-pricerange-cheap': ['cheap'],
    'inform-pricerange-moderate': ['moderately priced', 'moderate'],
    'inform-pricerange-expensive': ['expensive'],
    'confirm-pricerange-cheap': ['is it cheap'],
    'confirm-pricerange-moderate': ['is it moderately priced', 'is it moderate'],
    'confirm-pricerange-expensive': ['is it expensive'],
    'deny-pricerange-cheap': ['not cheap'],
    'deny-pricerange-moderate': ['no moderately priced', 'not moderate'],
    'deny-pricerange-expensive': ['not expensive'],

    'inform-this-dontcare': ['dont care', 'i dont mind', 'any', 'doesnt matter'],
    'inform-food-dontcare': ['any food', 'any type of food', 'any kind of food'],
    'inform-area-dontcare': ['any area', 'any part of town'],
    'inform-name-dontcare': ['any name'],
    'inform-pricerange-dontcare': ['dont care price range'],
    }

dstc3_templates = {

    'request-hastv': ['does it has a tv', 'does it has a television'],
    'request-childrenallowed': ['does it allow children'],
    'request-price': ['the price'],
    'request-hasinternet': ['does it have an internet connection'],
    'request-near': ['near'],
    'request-type': ['type of', 'what is the type'],

    'inform-hastv-true': ['has a television', 'with a television', 'television', 'tv'],
    'inform-hastv-false': ['no television', 'no tv'],
    'inform-childrenallowed-true': ['allows children', 'children allowed'],
    'inform-childrenallowed-false': ['not allow children', 'with no children'],
    'inform-hasinternet-true': ['with internet connection', 'has internet connection', 'with internet', 'has internet'],
    'inform-hasinternet-false': ['no internet connection', 'no internet'],

    'inform-hastv-dontcare': ['dont care tv', 'dont care television'],
    'inform-hasinternet-dontcare': ['dont care internet'],
    'inform-childrenallowed-dontcare': ['dont care children'],

    'inform-near-[near]': ['[near]'],
    'confirm-near-[near]': ['is it [near]'],
    'deny-near-[near]': ['not [near]'],

    'inform-area-[area]': ['[area]', '[area] area'],
    'confirm-area-[area]': ['is it in [area] area'],
    'deny-area-[area]': ['not [area] area'],

    'inform-type-restaurant': ['restaurant', 'looking for a restaurant'],
    'inform-type-pub': ['pub', 'looking for a pub'],
    'inform-type-coffeeshop': ['coffeeshop', 'coffee shop', 'cafe'],
    'confirm-type-restaurant': ['is it a restaurant'],
    'confirm-type-pub': ['pub', 'looking for a pub'],
    'confirm-type-coffeeshop': ['do they serve coffee', 'is it a coffee shop', 'is it a cafe'],
    'deny-type-restaurant': ['not restaurant'],
    'deny-type-pub': ['not pub'],
    'deny-type-coffeeshop': ['not coffeeshop', 'not cafe'],

    'inform-pricerange-free': ['free', 'free price range'],
    'confirm-pricerange-free': ['is it free'],
    'deny-pricerange-free': ['not free'],

    'inform-type-dontcare': ['any types'],
    'inform-near-dontcare': ['any where']
    }
