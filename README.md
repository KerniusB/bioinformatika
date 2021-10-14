# bioinformatika
<h1 align="center">
    Kernius Brazauskas 5 grupė, 1 pogrūpis
</h1>

Užduoties tikslas: įvertinti kodonų ir dikodonų dažnio skirtumus žinduolių ir bakterijų virusuose.

Programa turi:
* Pateiktoje sekoje fasta formatų surasti visas start ir stop kodonų poras, tarp kurių nebūtų stop kodono (ir tiesioginei sekai ir jos reverse komplementui). 
* Kiekvienam stop kodonui parinkti toliausiai nuo jo esanti start kodoną (su salyga, kad tarp jų nėra kito stop kodono)
* Atfiltruoti visus fragmentus ("tai būtų baltymų koduojancios sekos"), kurie trumpesni nei 100 fragmentų.
* Turėti funkcijas, kurios įvertintų kodonų ir dikodonų dažnius (visi imanomi kodonai/dikodonai ir jų atitinkamas dažnis)
* Palyginti kodonų bei dikodonų dažnius tarp visų sekų.

Taip pat reikia Įvertinti, ar bakteriniai ir žinduolių virusai sudaro atskirus klasterius vertinant kodonų/dikodonų dažnių aspektu.

<h2 align="center">
    Darbo aprašymas
</h2>

Pirmiausia buvo rastos visos įmanomos sekų kombinacijos. Tai buvo daryta, skaidant seką į tripletus nuo pirmo, antro arba trečio sekos nukleotido. Taip pat į tripletus galima skaidyti ir reverse komplementą, taigi iš viso susidarė 3*2=6 sekos. <br>
Toliau kiekvienoje iš 6 sekų buvo ieškoma orfų pradedant startiniu kodonu (ATG), bei užbaigiant stop kodonu (TAA, TAG, TGA). Atfiltruojami visi fragmentai, kurie turi mažiau nei 100 tripletų. Gautoje aibėje galima išsirinkti kodonus bei dikodonus, paskaičiuojamas jų dažnis dalinant jų keikį sekoje iš visų kodonų (arba dikodonų) skaičiaus.<br>
Taip pat daroma su visomis bakterijų ir žinduolių sekomis.<br>

<h2 align="center">
    Atstumų matricos skaičiavimas
</h2>
Paiimamos dviejų sekų kodonų (arba dikodonų) dažnių sekos, ir surandamas atitinkamų kodonų (arba dikodonų) skirtumas. Randamas gautos reikšmė modulis. Taip atitinkamai perėjus per visas dažnio eilėje reikšmes jos sumuojamos. <br>
Gauta reikšmė gali būti 0 ir daugiau. Pavyzdys paaiškinantis skaičiavimą:<br>
TTT pirmoje sekoje sudarė 0.02 visų tripletų, antroje sekoje 0.04, TTC pirmoje sekoje sudarė 0.06 visų tripletų, antroje sekoje 0.03, <br>
|(0.2) - (0.4)| + |(0.6) - (0.3)| + ...<br>


