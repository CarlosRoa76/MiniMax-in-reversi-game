import os
import csv

class Metrics:

    @staticmethod
    def generate_report(algorithm, opponent:str, winner:str, points:int, total_points:int):
        """Create the .csv file with the performance metrics."""
        
        # Métricas de rendimiento
        running_time = algorithm.ejecution_time
        max_ram_usage = algorithm.max_ram_usage
        search_depth = algorithm.depth_explored
        turns = algorithm.turns_played
        nodes_expanded = algorithm.nodes_expanded 

        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        
        csv_filename = os.path.join(output_dir, f"{algorithm.name}.csv")
        file_exists = os.path.isfile(csv_filename)
        
        with open(csv_filename, 'a', newline='') as f:
            writer = csv.writer(f)
            headers = ["opponent", "winner", "points", "Total_points", "turns", "total_nodes_expanded", "total_search_depth", "total_running_time", "total_max_ram_usage"]
            if not file_exists:
                writer.writerow(headers)
            
            row_data = [
                opponent,
                winner,
                points,
                total_points,
                turns,
                nodes_expanded,
                search_depth,
                f"{running_time:.2f}",
                f"{max_ram_usage:.2f}"
            ]
            writer.writerow(row_data)