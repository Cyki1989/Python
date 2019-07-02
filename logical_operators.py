isAutomaticMode = True
# is the level of day-lighr above 80%
is80PercentLight = True
# is the Sun ligthing directly into the driver's face
isDirectLight = False
# is it rainy, foggy or other weather conditions are present
isRainy = False

turnLightsOn=isAutomaticMode and (not is80PercentLight or isRainy or isDirectLight)

print("światła powinny się NIE świecić")

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = False

turnLightsOn=isAutomaticMode and (not is80PercentLight or isRainy or isDirectLight)

print("światła powinny się świecić")

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = True

turnLightsOn=isAutomaticMode and (not is80PercentLight or isRainy or isDirectLight)

print("światła powinny się świecić")

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

isAutomaticMode = True
is80PercentLight = True
isDirectLight = True
isRainy = False

turnLightsOn=isAutomaticMode and (not is80PercentLight or isRainy or isDirectLight)

print("światła powinny się świecić")

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = True

turnLightsOn=isAutomaticMode and (not is80PercentLight or isRainy or isDirectLight)

print("światła powinny się świecić")

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = True

turnLightsOn=isAutomaticMode and (not is80PercentLight or isRainy or isDirectLight)

print("światła powinny się NIE świecić")

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
