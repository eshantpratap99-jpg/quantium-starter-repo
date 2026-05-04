from dash.testing.composite import DashComposite
from app import app

# Test 1: Verify the header is present
def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)

# Test 2: Verify the visualisation is present
def test_vis_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)

# Test 3: Verify the region picker is present
def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=10)