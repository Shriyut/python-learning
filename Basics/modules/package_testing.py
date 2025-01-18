import feature.copyright
import feature.subfeature.calculator # from feature.subfeature import calculator
import feature.subfeature

# from Basics.modules.feature.copyright import year_of_copyright

print(feature.copyright.year_of_copyright)
# just import feature statement would result in an error since it would only know the content present in init file


print(feature.subfeature.calculator.subtract(9,8))

# calling add function mentioned in subfeature init
print(feature.subfeature.add(9,7))
print(feature.subfeature.creator)