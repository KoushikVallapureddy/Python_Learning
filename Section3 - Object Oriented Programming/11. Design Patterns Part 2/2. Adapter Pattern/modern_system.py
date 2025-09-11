from interfaces import DataProcessor, DataVisualizer

class AnalyticsSystem:
    """Modern analytics system that works with the new interfaces."""
    
    def __init__(self, data_processor: DataProcessor, data_visualizer: DataVisualizer):
        """Initialize with processor and visualizer components."""
        self.processor = data_processor
        self.visualizer = data_visualizer
        
    def analyze_and_visualize(self, data, output_file="output.png"):
        """Process data and create visualization."""
        # Process the data
        self.processor.process_data(data)
        results = self.processor.get_results()
        
        # Create visualization of the results
        # For simplicity, we'll visualize the original data
        # In a real system, you might visualize the results
        self.visualizer.visualize(data)
        self.visualizer.export_visualization(output_file)
        
        return {
            "analysis_results": results,
            "visualization_file": output_file
        }
        
    def get_analysis_summary(self):
        """Get a summary of the analysis results."""
        results = self.processor.get_results()
        if not results:
            return "No analysis results available"
            
        summary = []
        for key, value in results.items():
            if isinstance(value, (int, float)):
                summary.append(f"{key}: {value:.2f}")
            else:
                summary.append(f"{key}: {value}")
                
        return "\n".join(summary)
