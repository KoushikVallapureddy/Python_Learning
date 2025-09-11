from interfaces import DataProcessor, DataVisualizer
from legacy_system import LegacyDataAnalyzer, LegacyChartGenerator

class LegacyDataAnalyzerAdapter(DataProcessor):
    """Adapter for LegacyDataAnalyzer to work with the DataProcessor interface."""
    
    def __init__(self):
        self.legacy_analyzer = LegacyDataAnalyzer()
        
    def process_data(self, data):
        """Process data using the legacy analyzer."""
        if not isinstance(data, list):
            raise ValueError("Data must be a list of numeric values")
            
        if not all(isinstance(item, (int, float)) for item in data):
            raise ValueError("All data items must be numeric")
            
        self.legacy_analyzer.load_data(data)
        self.legacy_analyzer.run_analysis()
        return True
        
    def get_results(self):
        """Get results from the legacy analyzer."""
        results = self.legacy_analyzer.fetch_results()
        if results is None:
            return {}
        return results


class LegacyChartGeneratorAdapter(DataVisualizer):
    """Adapter for LegacyChartGenerator to work with the DataVisualizer interface."""
    
    def __init__(self, chart_type="bar"):
        self.legacy_chart_generator = LegacyChartGenerator()
        self.chart_type = chart_type
        self.legacy_chart_generator.initialize_chart(self.chart_type)
        
    def visualize(self, data):
        """Create visualization using the legacy chart generator."""
        if not isinstance(data, list):
            raise ValueError("Data must be a list of numeric values")
            
        if not all(isinstance(item, (int, float)) for item in data):
            raise ValueError("All data items must be numeric")
            
        self.legacy_chart_generator.add_data_series(data)
        success = self.legacy_chart_generator.render()
        return success
        
    def export_visualization(self, filename):
        """Export the visualization to a file using the legacy chart generator."""
        if not filename.endswith(('.png', '.jpg', '.pdf')):
            filename += '.png'  # Default to PNG if no extension
            
        return self.legacy_chart_generator.save_chart(filename)
