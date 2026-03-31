from django.db import models


class Candidate(models.Model):
    CANDIDATE_TYPE = [('New','New'),('Renewal','Renewal'),('Repeat','Repeat')]
    STATUS_CHOICES = [
        ('New','New'),('Documents Pending','Documents Pending'),
        ('Processing','Processing'),('Visa Applied','Visa Applied'),
        ('Approved','Approved'),('Ticket Booked','Ticket Booked'),
        ('Boarded','Boarded'),('Cancelled','Cancelled'),('Refunded','Refunded'),
    ]
    MEDICAL_CHOICES = [('Pending','Pending'),('Fit','Fit'),('Unfit','Unfit'),
                       ('Awaiting Report','Awaiting Report'),('Done','Done')]
    VISA_CHOICES = [('Not Applied','Not Applied'),('Applied','Applied'),
                    ('Approved','Approved'),('Rejected','Rejected'),('On Hold','On Hold')]
    TICKET_CHOICES = [('Not Booked','Not Booked'),('Booked','Booked'),
                      ('Confirmed','Confirmed'),('Cancelled','Cancelled')]
    RESUME_CHOICES = [('Not Received','Not Received'),('Received','Received'),('Uploaded','Uploaded')]
    PASSPORT_COPY_CHOICES = [('Not Received','Not Received'),('Soft Copy','Soft Copy'),
                             ('Original','Original'),('Both','Both')]
    OFFER_LETTER_CHOICES = [('Not Received','Not Received'),('Received','Received'),
                            ('Signed','Signed'),('Sent to Candidate','Sent to Candidate')]

    # 1. Candidate Name
    name = models.CharField(max_length=200)
    # 2. Phone
    phone = models.CharField(max_length=20)
    # 3. Passport Number
    passport_number = models.CharField(max_length=50, blank=True)
    # 4. Country (Destination)
    country = models.CharField(max_length=100, blank=True)
    # 5. Position / Job Role
    position = models.CharField(max_length=200, blank=True)
    # 6. Experience
    experience = models.CharField(max_length=100, blank=True)
    # 7. Status
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='New')
    # 8. Medical Status
    medical_status = models.CharField(max_length=30, choices=MEDICAL_CHOICES, default='Pending')
    # 9. Visa Status
    visa_status = models.CharField(max_length=30, choices=VISA_CHOICES, default='Not Applied')
    # 10. Ticket Status
    ticket_status = models.CharField(max_length=30, choices=TICKET_CHOICES, default='Not Booked')
    # 11. Payment
    payment = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 12. Resume
    resume_status = models.CharField(max_length=30, choices=RESUME_CHOICES, default='Not Received')
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True)
    # 13. Passport Copy
    passport_copy_status = models.CharField(max_length=30, choices=PASSPORT_COPY_CHOICES, default='Not Received')
    passport_copy_file = models.FileField(upload_to='passports/', blank=True, null=True)
    # 14. Offer Letter
    offer_letter_status = models.CharField(max_length=30, choices=OFFER_LETTER_CHOICES, default='Not Received')
    offer_letter_file = models.FileField(upload_to='offer_letters/', blank=True, null=True)
    # 15. Travel Date
    travel_date = models.DateField(null=True, blank=True)
    # 16. Reference
    reference = models.CharField(max_length=200, blank=True)
    # 17. Remarks
    remarks = models.TextField(blank=True)
    # 18. Follow-up Date
    followup_date = models.DateField(null=True, blank=True)
    # 19. Staff Name
    staff_name = models.CharField(max_length=100, blank=True)
    # 20. Registration Date
    registration_date = models.DateField(null=True, blank=True)

    candidate_type = models.CharField(max_length=20, choices=CANDIDATE_TYPE, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Application(models.Model):
    STATUS_CHOICES = [
        ('New','New'),('Documents Pending','Documents Pending'),
        ('Processing','Processing'),('Visa Applied','Visa Applied'),
        ('Approved','Approved'),('Ticket Booked','Ticket Booked'),
        ('Boarded','Boarded'),('Cancelled','Cancelled'),('Refunded','Refunded'),
    ]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    country = models.CharField(max_length=100, blank=True)
    job_category = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='New')
    application_date = models.DateField(null=True, blank=True)
    boarding_date = models.DateField(null=True, blank=True)
    package_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def balance(self):
        return self.package_amount - self.amount_paid

    def __str__(self):
        return f"{self.candidate.name} — {self.country}"

    class Meta:
        ordering = ['-created_at']


class Payment(models.Model):
    MODE_CHOICES = [('Cash','Cash'),('Bank Transfer','Bank Transfer'),
                    ('UPI','UPI'),('GPay','GPay'),('Cheque','Cheque'),('DD','DD')]
    PURPOSE_CHOICES = [('Registration Fee','Registration Fee'),('Visa Fee','Visa Fee'),
                       ('Air Ticket','Air Ticket'),('Documentation','Documentation'),
                       ('Training Fee','Training Fee'),('Miscellaneous','Miscellaneous')]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    mode = models.CharField(max_length=30, choices=MODE_CHOICES, default='Cash')
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES, default='Registration Fee')
    date = models.DateField()
    reference = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.name} — ₹{self.amount}"

    class Meta:
        ordering = ['-date']


class Invoice(models.Model):
    DOMAIN_CHOICES = [('Immigration','Immigration'),('Documentation','Documentation'),
                      ('Training','Training'),('Visit Visa','Visit Visa'),
                      ('Accommodation','Accommodation'),('B2B','B2B')]
    STATUS_CHOICES = [('Pending','Pending'),('Cleared','Cleared')]
    invoice_number = models.CharField(max_length=50, unique=True)
    domain = models.CharField(max_length=30, choices=DOMAIN_CHOICES, default='Immigration')
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True, related_name='invoices')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_number

    class Meta:
        ordering = ['-date']


class Document(models.Model):
    DOC_TYPES = [('Passport','Passport'),('Aadhaar','Aadhaar'),('PAN','PAN'),
                 ('Degree Certificate','Degree Certificate'),('School Certificate','School Certificate'),
                 ('Experience Letter','Experience Letter'),('Medical Certificate','Medical Certificate'),
                 ('Other','Other')]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='documents')
    doc_type = models.CharField(max_length=50, choices=DOC_TYPES)
    is_original = models.BooleanField(default=False)
    is_attested = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    with_company = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.name} — {self.doc_type}"

    class Meta:
        ordering = ['-date_added']


class CourierEntry(models.Model):
    TYPE_CHOICES = [('Inward','Inward'),('Outward','Outward')]
    entry_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True, related_name='couriers')
    from_person = models.CharField(max_length=200, blank=True)
    to_person = models.CharField(max_length=200, blank=True)
    courier_company = models.CharField(max_length=100, blank=True)
    tracking_number = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    contents = models.CharField(max_length=200, blank=True)
    handled_by = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entry_type} — {self.tracking_number}"

    class Meta:
        ordering = ['-date']


class LegalRecord(models.Model):
    CANCELLATION_CHOICES = [('No','No'),('Pending','Pending'),('Approved','Approved')]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='legal_records')
    agreement_signed = models.BooleanField(default=False)
    sop_shared = models.BooleanField(default=False)
    terms_accepted = models.BooleanField(default=False)
    refund_eligible = models.BooleanField(default=False)
    refund_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    refund_date = models.DateField(null=True, blank=True)
    cancellation_status = models.CharField(max_length=20, choices=CANCELLATION_CHOICES, default='No')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Legal — {self.candidate.name}"

    class Meta:
        ordering = ['-created_at']


class B2BClient(models.Model):
    CONTRACT_CHOICES = [('Pending','Pending'),('Signed','Signed'),
                        ('Active','Active'),('Expired','Expired')]
    company_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    contract_status = models.CharField(max_length=20, choices=CONTRACT_CHOICES, default='Pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ['-created_at']

# for hotel booking
class HotelBooking(models.Model):

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='hotel_bookings'
    )

    hotel_name = models.CharField(
        max_length=200
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    check_in = models.DateTimeField()

    check_out = models.DateTimeField()

    room_number = models.CharField(
        max_length=50,
        blank=True
    )

    booking_reference = models.CharField(
        max_length=100,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    amount_paid = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    @property
    def balance(self):

        return self.amount - self.amount_paid


    def __str__(self):

        return f"{self.candidate.name} — {self.hotel_name}"


    class Meta:

        ordering = ['check_out']

class FlightBooking(models.Model):

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='flight_bookings'
    )

    airline = models.CharField(
        max_length=200
    )

    from_city = models.CharField(
        max_length=100
    )

    to_city = models.CharField(
        max_length=100
    )

    departure_date =models.DateTimeField()

    arrival_date =models.DateTimeField()

    ticket_number =models.CharField(
        max_length=100,
        blank=True
    )

    pnr =models.CharField(
        max_length=100,
        blank=True
    )

    amount =models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    paid =models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    reminder_sent = models.BooleanField(default=False)

    notes =models.TextField(blank=True)

    created_at =models.DateTimeField(auto_now_add=True)


    @property
    def balance(self):

        return self.amount - self.paid


    def __str__(self):

        return f"{self.candidate.name} - {self.airline}"