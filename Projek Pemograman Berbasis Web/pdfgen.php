<?php
require('./fpdf.php');

$pdf = new FPDF();
$title = 'Biodata Diri';
$profile = './src/PP.png';

$centerX = $pdf->GetPageWidth() / 2;
$biodata = array(
    "Nama" => 'Maull aja',
    "NIM" => '123456',
    "Jenis Kelamin" => "Pria",
    "Tempat Lahir" => 'kota',
    "Tanggal Lahir" => 'ada aja',
    "Email" => 'awokwokwokw@',
    "Telepon" => '08123456',
    "Program Studi" => 'jurusan',
);


$pdf->AddPage();
$pdf->SetFont('Arial', 'B', 12);
$pdf->SetXY($centerX - $pdf->GetStringWidth($title) / 2, 10);
$pdf->Cell(40, 10, $title);
$pdf->SetXY(30, 30);
$pdf->Image($profile, null, null, 50, 50);
$pdf->SetXY($centerX, 30);

foreach ($biodata as $field=>$value) {
    $pdf->SetX($centerX);
    $pdf->SetFont('Arial', '', 10);
    $pdf->Cell(40, 10, $field);
    $pdf->Ln(5);
    $pdf->SetX($centerX);
    $pdf->SetFont('Arial', 'B', 10);
    $pdf->Cell(40, 10, $value);
    $pdf->Ln();
}

$pdf->Output();
?>