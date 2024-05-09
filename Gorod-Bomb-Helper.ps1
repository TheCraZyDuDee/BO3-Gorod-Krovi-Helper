Add-Type -AssemblyName System.Windows.Forms

# create a form
$form = New-Object System.Windows.Forms.Form
$form.Text = "Gorod Bomb Helper"
$form.Size = New-Object System.Drawing.Size(315,350)
$form.StartPosition = "CenterScreen"

# main lable
$label = New-Object System.Windows.Forms.Label
$label.Location = New-Object System.Drawing.Point(10,20)
$label.Size = New-Object System.Drawing.Size(280,20)
$label.Text = "Select Locations in order to remember them"

# lable for version number
$label2 = New-Object System.Windows.Forms.Label
$label2.Location = New-Object System.Drawing.Point(10,290)
$label2.Size = New-Object System.Drawing.Size(280,20)
$label2.Text = "v0.0.1"

# Initialize counters
$script:counter = 0

# Create buttons for each option
$button1 = New-Object System.Windows.Forms.Button
$button1.Location = New-Object System.Drawing.Point(10,50)
$button1.Size = New-Object System.Drawing.Size(280,23)
$button1.Text = "Tank Factory"
$button1.Add_Click({
    $script:counter++
    $label.Text = "Tank Factory - $script:counter"
    $button1.Text = "Tank Factory ($script:counter)"
    $button1.Enabled = $false
    if ($script:counter -eq 6) {
        DisableAllButtons
    }
})

$button2 = New-Object System.Windows.Forms.Button
$button2.Location = New-Object System.Drawing.Point(10,80)
$button2.Size = New-Object System.Drawing.Size(280,23)
$button2.Text = "Dragon Command"
$button2.Add_Click({
    $script:counter++
    $label.Text = "Dragon Command - $script:counter"
    $button2.Text = "Dragon Command ($script:counter)"
    $button2.Enabled = $false
    if ($script:counter -eq 6) {
        DisableAllButtons
    }
})

$button3 = New-Object System.Windows.Forms.Button
$button3.Location = New-Object System.Drawing.Point(10,110)
$button3.Size = New-Object System.Drawing.Size(280,23)
$button3.Text = "Infarmy"
$button3.Add_Click({
    $script:counter++
    $label.Text = "Infarmy - $script:counter"
    $button3.Text = "Infarmy ($script:counter)"
    $button3.Enabled = $false
    if ($script:counter -eq 6) {
        DisableAllButtons
    }
})

$button4 = New-Object System.Windows.Forms.Button
$button4.Location = New-Object System.Drawing.Point(10,140)
$button4.Size = New-Object System.Drawing.Size(280,23)
$button4.Text = "Armory"
$button4.Add_Click({
    $script:counter++
    $label.Text = "Armory - $script:counter"
    $button4.Text = "Armory ($script:counter)"
    $button4.Enabled = $false
    if ($script:counter -eq 6) {
        DisableAllButtons
    }
})

$button5 = New-Object System.Windows.Forms.Button
$button5.Location = New-Object System.Drawing.Point(10,170)
$button5.Size = New-Object System.Drawing.Size(280,23)
$button5.Text = "Supply Depot"
$button5.Add_Click({
    $script:counter++
    $label.Text = "Supply Depot - $script:counter"
    $button5.Text = "Supply Depot ($script:counter)"
    $button5.Enabled = $false
    if ($script:counter -eq 6) {
        DisableAllButtons
    }
})

$button6 = New-Object System.Windows.Forms.Button
$button6.Location = New-Object System.Drawing.Point(10,200)
$button6.Size = New-Object System.Drawing.Size(280,23)
$button6.Text = "Dept. Store"
$button6.Add_Click({
    $script:counter++
    $label.Text = "Dept. Store - $script:counter"
    $button6.Text = "Dept. Store ($script:counter)"
    $button6.Enabled = $false
    if ($script:counter -eq 6) {
        DisableAllButtons
    }
})

# Create a reset button
$resetButton = New-Object System.Windows.Forms.Button
$resetButton.Location = New-Object System.Drawing.Point(10,250)
$resetButton.Size = New-Object System.Drawing.Size(50,23)
$resetButton.Text = "Reset"
$resetButton.Add_Click({
    $script:counter = 0
    $label.Text = "Select Locations in order to remember them"
    $button1.Text = "Tank Factory"
    $button2.Text = "Dragon Command"
    $button3.Text = "Infarmy"
    $button4.Text = "Armory"
    $button5.Text = "Supply Depot"
    $button6.Text = "Dept. Store"
    EnableAllButtons
})

# Define a function to disable all buttons except the reset button
function DisableAllButtons {
    $button1.Enabled = $false
    $button2.Enabled = $false
    $button3.Enabled = $false
    $button4.Enabled = $false
    $button5.Enabled = $false
    $button6.Enabled = $false
}

# Define a function to enable all buttons
function EnableAllButtons {
    $button1.Enabled = $true
    $button2.Enabled = $true
    $button3.Enabled = $true
    $button4.Enabled = $true
    $button5.Enabled = $true
    $button6.Enabled = $true
}

# Add controls to the form
$form.Controls.Add($label)
$form.Controls.Add($label2)
$form.Controls.Add($button1)
$form.Controls.Add($button2)
$form.Controls.Add($button3)
$form.Controls.Add($button4)
$form.Controls.Add($button5)
$form.Controls.Add($button6)
$form.Controls.Add($resetButton)

# Show the form
$form.ShowDialog() | Out-Null
