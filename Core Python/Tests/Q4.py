area = float(input("Enter area of one wall: "))
i_cost = float(input("Enter interior wall cost: "))
e_cost = float(input("Enter exterior wall cost: "))

interior = area * 8 * i_cost
exterior = area * 6 * e_cost

total = interior + exterior

print("Interior Painting Cost:", interior)
print("Exterior Painting Cost:", exterior)
print("Total Painting Cost:", total)