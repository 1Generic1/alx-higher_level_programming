document.addEventListener('DOMContentLoaded', function() {
  $('#add_item').click(function() {
    $('UL.my_list').append('<li>Item</li>');
  });
  // Remove the last item from the list
  $('#remove_item').click(function() {
    $('UL.my_list li:last-child').remove();
  });
  // Clear all items from the list
  $('#clear_list').click(function() {
    $('UL.my_list').empty();
  });
});
