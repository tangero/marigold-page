---
slug: "aac-eld"
url: "/mobilnisite/slovnik/aac-eld/"
type: "slovnik"
title: "AAC-ELD – Advanced Audio Coding – Enhanced Low Delay"
date: 2025-01-01
abbr: "AAC-ELD"
fullName: "Advanced Audio Coding – Enhanced Low Delay"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aac-eld/"
summary: "AAC-ELD je nízkolatenční audio kodek standardizovaný organizací 3GPP pro služby komunikace v reálném čase. Kombinuje vysokou kompresní efektivitu AAC-LD s replikací spektrálního pásma (SBR) pro zajišt"
---

AAC-ELD je nízkolatenční audio kodek standardizovaný organizací 3GPP, který kombinuje efektivitu AAC-LD s technikou replikace spektrálního pásma (SBR) pro zajištění zvuku kvality CD s minimálním zpožděním pro komunikaci v reálném čase přes mobilní sítě.

## Popis

Advanced Audio Coding – Enhanced Low Delay (AAC-ELD, pokročilé kódování zvuku s vylepšeným nízkým zpožděním) je sofistikovaná technologie kódování zvuku standardizovaná v dokumentu 3GPP TS 26.923, která řeší kritickou potřebu přenosu vysokokvalitního zvuku s nízkou latencí v mobilních komunikačních systémech. Kodek funguje na principu hybridního kódování, které kombinuje základní transformační kódování AAC-LD (Low Delay) s technikami replikace spektrálního pásma (SBR) a parametrického sterea (PS). Tato architektura umožňuje efektivní kompresi při zachování věrnosti zvuku a minimalizaci algoritmického zpoždění na přibližně 15–32 milisekund, což je zásadní pro obousměrnou komunikaci v reálném čase, kde musí celkové zpoždění od konce ke konci zůstat pod 150 milisekund, aby se předešlo vnímatelnému echu a narušení konverzace.

Technický základ AAC-ELD využívá modifikovanou diskrétní kosinovou transformaci (MDCT) s délkou rámce optimalizovanou pro nízkou latenci, typicky 512 nebo 480 vzorků při vzorkovací frekvenci 48 kHz. Kodek zahrnuje několik pokročilých komponent, včetně psychoakustického modelu, který analyzuje audio signály za účelem stanovení prahů maskování, což mu umožňuje efektivně alokovat bity odstraněním percepčně nevýznamných informací. Komponenta SBR rozšiřuje šířku pásma vysokých frekvencí přenosem pouze malého množství doplňkových informací, které umožňují dekodéru rekonstruovat vysokofrekvenční obsah z nižších frekvenčních pásem, čímž výrazně zlepšuje kompresní efektivitu bez zvýšení zpoždění.

Fungování kodeku zahrnuje několik zpracovatelských stupňů: časově-frekvenční transformaci pomocí MDCT, kvantizaci založenou na psychoakustickém modelování, Huffmanovo kódování pro redukci entropie a extrakci parametrů SBR/PS. Pro stereofonní obsah může AAC-ELD pracovat buď v režimu pravého sterea, nebo v režimu parametrického sterea, kde jsou prostorové informace kódovány jako kompaktní parametry namísto úplných informací o kanálech. Dekodér provádí inverzní operace včetně Huffmanova dekódování, inverzní kvantizace, inverzní MDCT transformace a SBR syntézy pro rekonstrukci audio signálu. Tento komplexní přístup umožňuje AAC-ELD poskytovat téměř transparentní kvalitu zvuku při datových tocích v rozsahu od 24 do 64 kbps při zachování nízké latence nezbytné pro konverzační aplikace.

V rámci sítí 3GPP slouží AAC-ELD jako klíčový prvek pro služby vylepšeného hlasu (EVS) a další multimediální aplikace v reálném čase. Integruje se s architekturou IMS (IP Multimedia Subsystem) prostřednictvím definovaných procedur vyjednávání kodeků v signalizaci SIP/SDP, což koncovým bodům umožňuje vybrat optimální audio kodek na základě síťových podmínek a možností zařízení. Robustní mechanismy pro maskování chyb a odolnost vůči ztrátě paketů činí tento kodek zvláště vhodným pro bezdrátový přenos, kde jsou ztráty paketů a kolísání zpoždění běžné, a zajišťují tak konzistentní kvalitu zvuku i v náročných síťových podmínkách.

## K čemu slouží

AAC-ELD byl vyvinut, aby řešil rostoucí poptávku po vysokokvalitní audio komunikaci s nízkou latencí v mobilních sítích, zejména pro služby jako Voice over LTE (VoLTE), videokonference a interaktivní multimediální aplikace. Před jeho zavedením čelily mobilní audio kodeky zásadnímu kompromisu mezi kompresní efektivitou, kvalitou zvuku a algoritmickým zpožděním. Tradiční kodeky jako AMR-WB poskytovaly přijatelnou latenci, ale omezenou šířku pásma zvuku, zatímco vysoce efektivní kodeky jako HE-AAC zaváděly pro konverzační aplikace nepřijatelné zpoždění. Toto omezení se stávalo stále problematičtějším, jak se mobilní sítě vyvíjely k podpoře bohatších multimediálních služeb, které vyžadovaly jak vysokou věrnost, tak interakci v reálném čase.

Vytvoření AAC-ELD bylo motivováno několika konkrétními omezeními existujících přístupů. Standardní AAC kodeky, ačkoli nabízely vynikající kompresní efektivitu, typicky zaváděly algoritmická zpoždění 100–200 milisekund kvůli použití dlouhých transformačních oken a vyrovnávacích pamětí pro pohled vpřed. To je činilo nevhodnými pro obousměrnou komunikaci, kde musí celkové zpoždění od konce ke konci zůstat pod 150 milisekund, aby byl zachován přirozený průběh konverzace. Zatímco specializované nízkolatenční kodeky jako G.722.1 nabízely minimální latenci, ale trpěly horší kompresní efektivitou a kvalitou zvuku ve srovnání s moderními transformačními kodeky.

Organizace 3GPP uznala, že vznikající služby jako vysoce kvalitní hlas, videohovory a hraní her v reálném čase vyžadují nové řešení pro kódování zvuku, které by tuto mezeru překlenulo. AAC-ELD tyto požadavky řeší specificky kombinací efektivity transformačního kódování AAC s inovativními optimalizacemi pro nízké zpoždění a technikami rozšíření pásma. Jeho vývoj byl poháněn vývojem mobilních sítí směrem k plně IP architekturám, kde se hlasové a multimediální služby sbližují, což vytváří potřebu jednotného audio kodeku schopného poskytovat zvuk studiové kvality s konverzační latencí při efektivním využití dostupné síťové kapacity.

## Klíčové vlastnosti

- Algoritmické zpoždění 15–32 milisekund umožňující přirozenou konverzaci
- Replikace spektrálního pásma (SBR) pro efektivní kódování vysokých frekvencí
- Podpora parametrického sterea (PS) pro prostorový zvuk při nízkých datových tocích
- Rozsah datového toku od 24 do 64 kbps s škálovatelnou kvalitou
- Robustní maskování chyb pro odolnost vůči ztrátě paketů
- Zpětná kompatibilita s dekodéry AAC-LD

## Definující specifikace

- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling

---

📖 **Anglický originál a plná specifikace:** [AAC-ELD na 3GPP Explorer](https://3gpp-explorer.com/glossary/aac-eld/)
