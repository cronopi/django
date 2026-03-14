"""
Comprehensive tests for the Page class.
Tests cover all validation rules and Page functionality.
"""

from Page import Page
from elements import (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td,
                      Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br)
from elem import Text, Elem


def test_valid_basic_html_structure():
	"""Test 1: Valid basic HTML structure."""
	print("\n=== Test 1: Valid Basic HTML Structure ===")
	
	html = Html([
		Head(Title(Text("My Page"))),
		Body(H1(Text("Welcome")))
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: True)")
	assert is_valid == True, "Basic HTML should be valid"
	print("✓ PASSED")


def test_valid_complex_html():
	"""Test 2: Valid complex HTML with multiple elements."""
	print("\n=== Test 2: Valid Complex HTML ===")
	
	html = Html([
		Head([
			Title(Text("Complete Page")),
			Meta(charset="utf-8")
		]),
		Body([
			H1(Text("Main Title")),
			H2(Text("Subtitle")),
			P(Text("This is a paragraph.")),
			Div([
				Span(Text("Highlighted text")),
				P(Text("Paragraph inside span"))
			]),
			Ul([
				Li(Text("Item 1")),
				Li(Text("Item 2")),
				Li(Text("Item 3"))
			]),
			Table([
				Tr([
					Th(Text("Header 1")),
					Th(Text("Header 2"))
				]),
				Tr([
					Td(Text("Cell 1")),
					Td(Text("Cell 2"))
				])
			])
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: True)")
	assert is_valid == True, "Complex HTML should be valid"
	print("✓ PASSED")


def test_invalid_html_no_head_body():
	"""Test 3: Invalid - Html without Head and Body."""
	print("\n=== Test 3: Invalid - Html without Head and Body ===")
	
	html = Html([
		H1(Text("Just a header"))  # Missing Head, Body
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Html without Head and Body should be invalid"
	print("✓ PASSED")


def test_invalid_html_wrong_order():
	"""Test 4: Invalid - Html with Body before Head."""
	print("\n=== Test 4: Invalid - Html with Body before Head ===")
	
	html = Html([
		Body(H1(Text("Body first"))),
		Head(Title(Text("Head second")))
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Html with wrong order should be invalid"
	print("✓ PASSED")


def test_invalid_head_without_title():
	"""Test 5: Invalid - Head without Title."""
	print("\n=== Test 5: Invalid - Head without Title ===")
	
	html = Html([
		Head(Meta(charset="utf-8")),  # No Title
		Body(H1(Text("Content")))
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Head without Title should be invalid"
	print("✓ PASSED")


def test_invalid_head_multiple_titles():
	"""Test 6: Invalid - Head with multiple Titles."""
	print("\n=== Test 6: Invalid - Head with multiple Titles ===")
	
	html = Html([
		Head([
			Title(Text("First Title")),
			Title(Text("Second Title"))
		]),
		Body(H1(Text("Content")))
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Head with multiple Titles should be invalid"
	print("✓ PASSED")


def test_invalid_body_contains_title():
	"""Test 7: Invalid - Body contains Title (not allowed)."""
	print("\n=== Test 7: Invalid - Body contains Title ===")
	
	html = Html([
		Head(Title(Text("Valid Title"))),
		Body([
			Title(Text("Invalid Title in Body")),
			H1(Text("Header"))
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Body should not contain Title"
	print("✓ PASSED")


def test_invalid_title_contains_element():
	"""Test 8: Invalid - Title contains Elem instead of Text."""
	print("\n=== Test 8: Invalid - Title contains Elem instead of Text ===")
	
	html = Html([
		Head(Title(H1(Text("Title with H1")))),  # Only Text allowed in Title
		Body(H1(Text("Content")))
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Title should contain only Text"
	print("✓ PASSED")


def test_invalid_title_empty():
	"""Test 9: Invalid - Title without content."""
	print("\n=== Test 9: Invalid - Title without content ===")
	
	html = Html([
		Head(Title()),  # Empty title
		Body(H1(Text("Content")))
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Title must contain exactly one Text"
	print("✓ PASSED")


def test_invalid_p_contains_element():
	"""Test 10: Invalid - P contains Elem instead of Text."""
	print("\n=== Test 10: Invalid - P contains Elem instead of Text ===")
	
	html = Html([
		Head(Title(Text("Page"))),
		Body([
			P(Span(Text("Invalid")))  # Only Text allowed in P
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "P should contain only Text"
	print("✓ PASSED")


def test_invalid_span_contains_text_and_p():
	"""Test 11: Valid - Span can contain Text and P."""
	print("\n=== Test 11: Valid - Span can contain Text and P ===")
	
	html = Html([
		Head(Title(Text("Page"))),
		Body([
			Span([
				Text("Regular text"),
				P(Text("Paragraph in span"))
			])
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: True)")
	assert is_valid == True, "Span should accept Text and P"
	print("✓ PASSED")


def test_invalid_ul_without_li():
	"""Test 12: Invalid - Ul without Li elements."""
	print("\n=== Test 12: Invalid - Ul without Li elements ===")
	
	html = Html([
		Head(Title(Text("Page"))),
		Body([
			Ul()  # No Li elements
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Ul must contain at least one Li"
	print("✓ PASSED")


def test_invalid_ul_with_non_li_elements():
	"""Test 13: Invalid - Ul contains non-Li elements."""
	print("\n=== Test 13: Invalid - Ul contains non-Li elements ===")
	
	html = Html([
		Head(Title(Text("Page"))),
		Body([
			Ul([
				Li(Text("Item 1")),
				H1(Text("Invalid header in list"))
			])
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Ul should contain only Li"
	print("✓ PASSED")


def test_valid_ol_with_li():
	"""Test 14: Valid - Ol with Li elements."""
	print("\n=== Test 14: Valid - Ol with Li elements ===")
	
	html = Html([
		Head(Title(Text("Page"))),
		Body([
			Ol([
				Li(Text("First")),
				Li(Text("Second")),
				Li(Text("Third"))
			])
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: True)")
	assert is_valid == True, "Ol with Li should be valid"
	print("✓ PASSED")


def test_invalid_tr_without_th_td():
	"""Test 15: Invalid - Tr without Th or Td."""
	print("\n=== Test 15: Invalid - Tr without Th or Td ===")
	
	html = Html([
		Head(Title(Text("Page"))),
		Body([
			Table([
				Tr(H1(Text("Invalid")))
			])
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Tr must contain Th or Td"
	print("✓ PASSED")


def test_invalid_tr_mixed_th_td():
	"""Test 16: Invalid - Tr with both Th and Td (must be exclusive)."""
	print("\n=== Test 16: Invalid - Tr with both Th and Td ===")
	
	html = Html([
		Head(Title(Text("Page"))),
		Body([
			Table([
				Tr([
					Th(Text("Header")),
					Td(Text("Data"))  # Can't mix Th and Td
				])
			])
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Tr cannot mix Th and Td"
	print("✓ PASSED")


def test_valid_tr_only_th():
	"""Test 17: Valid - Tr with only Th elements."""
	print("\n=== Test 17: Valid - Tr with only Th elements ===")
	
	html = Html([
		Head(Title(Text("Page"))),
		Body([
			Table([
				Tr([
					Th(Text("Header 1")),
					Th(Text("Header 2"))
				])
			])
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: True)")
	assert is_valid == True, "Tr with only Th should be valid"
	print("✓ PASSED")


def test_valid_table_with_complete_rows():
	"""Test 18: Valid - Complete table with header and body rows."""
	print("\n=== Test 18: Valid - Complete table ===")
	
	html = Html([
		Head(Title(Text("Page"))),
		Body([
			Table([
				Tr([
					Th(Text("Name")),
					Th(Text("Value"))
				]),
				Tr([
					Td(Text("Python")),
					Td(Text("Language"))
				]),
				Tr([
					Td(Text("HTML")),
					Td(Text("Markup"))
				])
			])
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: True)")
	assert is_valid == True, "Complete table should be valid"
	print("✓ PASSED")


def test_invalid_invalid_tag():
	"""Test 19: Invalid - Non-allowed tag in tree."""
	print("\n=== Test 19: Invalid - Non-allowed tag ===")
	
	# Create custom Elem with invalid tag
	invalid = Elem(tag='invalid_tag', content=Text("Text"))
	html = Html([
		Head(Title(Text("Page"))),
		Body(invalid)
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: False)")
	assert is_valid == False, "Invalid tag should be rejected"
	print("✓ PASSED")


def test_page_str_with_doctype():
	"""Test 20: __str__ method includes doctype for Html root."""
	print("\n=== Test 20: __str__ with doctype ===")
	
	html = Html([
		Head(Title(Text("Test Page"))),
		Body(H1(Text("Content")))
	])
	
	page = Page(html)
	html_str = str(page)
	
	has_doctype = html_str.startswith('<!DOCTYPE html>')
	print(f"Has doctype: {has_doctype} (expected: True)")
	assert has_doctype, "__str__ should include doctype for Html root"
	print("✓ PASSED")
	print(f"\nGenerated HTML:\n{html_str[:200]}...")


def test_page_write_to_file():
	"""Test 21: write_to_file method creates file with doctype."""
	print("\n=== Test 21: write_to_file method ===")
	
	html = Html([
		Head(Title(Text("File Test"))),
		Body([
			H1(Text("Welcome")),
			P(Text("This is a test page."))
		])
	])
	
	page = Page(html)
	filename = "/tmp/test_page.html"
	
	page.write_to_file(filename)
	
	with open(filename, 'r', encoding='utf-8') as f:
		content = f.read()
	
	has_doctype = content.startswith('<!DOCTYPE html>')
	print(f"File created with doctype: {has_doctype} (expected: True)")
	assert has_doctype, "File should include doctype"
	print(f"File written successfully to {filename}")
	print("✓ PASSED")


def test_nested_div_and_spans():
	"""Test 22: Valid - Nested divs with various allowed elements."""
	print("\n=== Test 22: Valid - Nested divs ===")
	
	html = Html([
		Head(Title(Text("Div Test"))),
		Body([
			Div([
				H1(Text("Section 1")),
				Span(Text("Highlighted")),
				Div([
					H2(Text("Subsection")),
					Span([
						Text("Text"),
						P(Text("Paragraph"))
					])
				])
			])
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: True)")
	assert is_valid == True, "Nested divs should be valid"
	print("✓ PASSED")


def test_self_closing_elements():
	"""Test 23: Valid - Self-closing elements (Br, Hr, Img)."""
	print("\n=== Test 23: Valid - Self-closing elements ===")
	
	html = Html([
		Head([
			Title(Text("Selfclosing Test")),
			Meta(charset="utf-8")
		]),
		Body([
			H1(Text("Title")),
			Hr(),
			P(Text("Paragraph")),
			Br(),
			Img(src="image.jpg", alt="example")
		])
	])
	
	page = Page(html)
	is_valid = page.is_valid()
	print(f"Valid: {is_valid} (expected: True)")
	assert is_valid == True, "Self-closing elements should be valid"
	print("✓ PASSED")


def test_invalid_page_initialization():
	"""Test 24: Invalid - Page initialization with wrong type."""
	print("\n=== Test 24: Invalid - Page initialization with wrong type ===")
	
	try:
		page = Page("not an element")
		print("ERROR: Should have raised ValueError")
		assert False, "Should raise ValueError for non-Elem input"
	except ValueError as e:
		print(f"Correctly raised ValueError: {e}")
		print("✓ PASSED")


def run_all_tests():
	"""Run all tests."""
	print("\n" + "="*60)
	print("RUNNING ALL PAGE CLASS TESTS")
	print("="*60)
	
	tests = [
		test_valid_basic_html_structure,
		test_valid_complex_html,
		test_invalid_html_no_head_body,
		test_invalid_html_wrong_order,
		test_invalid_head_without_title,
		test_invalid_head_multiple_titles,
		test_invalid_body_contains_title,
		test_invalid_title_contains_element,
		test_invalid_title_empty,
		test_invalid_p_contains_element,
		test_invalid_span_contains_text_and_p,
		test_invalid_ul_without_li,
		test_invalid_ul_with_non_li_elements,
		test_valid_ol_with_li,
		test_invalid_tr_without_th_td,
		test_invalid_tr_mixed_th_td,
		test_valid_tr_only_th,
		test_valid_table_with_complete_rows,
		test_invalid_invalid_tag,
		test_page_str_with_doctype,
		test_page_write_to_file,
		test_nested_div_and_spans,
		test_self_closing_elements,
		test_invalid_page_initialization,
	]
	
	passed = 0
	failed = 0
	
	for test in tests:
		try:
			test()
			passed += 1
		except AssertionError as e:
			print(f"✗ FAILED: {e}")
			failed += 1
		except Exception as e:
			print(f"✗ ERROR: {e}")
			failed += 1
	
	print("\n" + "="*60)
	print(f"RESULTS: {passed} passed, {failed} failed out of {len(tests)} tests")
	print("="*60)
	
	return failed == 0


if __name__ == '__main__':
	success = run_all_tests()
	exit(0 if success else 1)
