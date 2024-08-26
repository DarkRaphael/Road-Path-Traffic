class City:
    def __init__(self, name, supply, demand):
        self.name = name
        self.supply = supply
        self.demand = demand
        self.satisfied_demand = 0
        self.utilized_supply = 0

class Road:
    def __init__(self, city1, city2, cost):
        self.city1 = city1
        self.city2 = city2
        self.cost = cost

def create_roads(cities, costs):
    roads = []
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            cost = costs[i][j]
            road = Road(cities[i], cities[j], cost)
            roads.append(road)
    return roads

def meet_demand_and_supply(roads):
    total_demand = sum(city.demand for city in cities)
    total_supply = sum(city.supply for city in cities)
    
    required_demand_met = total_demand * 0.8
    required_supply_utilized = total_supply * 0.8
    
    total_demand_met = 0
    total_supply_utilized = 0

    for road in roads:
        if total_demand_met >= required_demand_met and total_supply_utilized >= required_supply_utilized:
            break
        
        supply_from_city1 = road.city1.supply
        demand_from_city2 = road.city2.demand - road.city2.satisfied_demand

        if demand_from_city2 > 0:
            demand_to_satisfy = min(supply_from_city1, demand_from_city2)
            road.city1.supply -= demand_to_satisfy
            road.city2.satisfied_demand += demand_to_satisfy
            total_demand_met += demand_to_satisfy
            total_supply_utilized += demand_to_satisfy

            # Additional check for costs
            if road.cost < 100000000:  # Less than 1 Crore
                additional_supply = min(demand_to_satisfy * 0.05, road.city1.supply)
                road.city1.supply -= additional_supply
                road.city2.satisfied_demand += additional_supply
                total_demand_met += additional_supply
                total_supply_utilized += additional_supply

    return total_demand_met, total_supply_utilized

def display_results(cities, total_demand_met, total_supply_utilized):
    print("City Demand and Supply Satisfaction:")
    for city in cities:
        print(f"{city.name}: Demand = {city.demand}, Satisfied Demand = {city.satisfied_demand}, Supply = {city.supply}, Utilized Supply = {city.utilized_supply}")
    
    print(f"\nTotal Demand Met: {total_demand_met}")
    print(f"Total Supply Utilized: {total_supply_utilized}")

def main():
    # Define cities with their supply and demand
    global cities
    cities = [
        City("City A", supply=100, demand=80),
        City("City B", supply=60, demand=90),
        City("City C", supply=70, demand=50),
    ]

    # Define cost matrix for building roads between cities
    costs = [
        [0, 50000000, 70000000],  # Costs from City A to others
        [50000000, 0, 40000000],   # Costs from City B to others
        [70000000, 40000000, 0],   # Costs from City C to others
    ]

    # Create roads based on supply, demand, and cost
    roads = create_roads(cities, costs)

    # Meet demand and supply based on the conditions
    total_demand_met, total_supply_utilized = meet_demand_and_supply(roads)

    # Display the results
    display_results(cities, total_demand_met, total_supply_utilized)

if __name__ == "__main__":
    main()
