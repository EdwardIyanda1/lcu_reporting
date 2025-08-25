// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    // Handle report form submission with AJAX
    const reportForm = document.getElementById('report-form');
    if (reportForm) {
        reportForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(reportForm);
            
            fetch(reportForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Show confirmation modal
                    document.getElementById('confirmation-modal').style.display = 'flex';
                    reportForm.reset();
                } else {
                    // Handle form errors
                    alert('There was an error submitting your report. Please try again.');
                    if (data.errors) {
                        console.error(data.errors);
                    }
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('There was an error submitting your report. Please try again.');
            });
        });
    }

    // Modal handling
    const modal = document.getElementById('confirmation-modal');
    if (modal) {
        const closeModal = document.querySelector('.close-modal');
        const modalOkBtn = document.getElementById('modal-ok-btn');
        
        if (closeModal) {
            closeModal.addEventListener('click', () => {
                modal.style.display = 'none';
                window.location.href = '/';
            });
        }
        
        if (modalOkBtn) {
            modalOkBtn.addEventListener('click', () => {
                modal.style.display = 'none';
                window.location.href = '/';
            });
        }
        
        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
                window.location.href = '/';
            }
        });
    }
});