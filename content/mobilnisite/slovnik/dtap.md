---
slug: "dtap"
url: "/mobilnisite/slovnik/dtap/"
type: "slovnik"
title: "DTAP – Direct Transfer Application Part"
date: 2025-01-01
abbr: "DTAP"
fullName: "Direct Transfer Application Part"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dtap/"
summary: "DTAP je protokol jádrové sítě používaný pro transparentní přenos signalizačních zpráv nesouvisejících s hovorem, jako jsou zprávy správy mobility a správy relací, mezi mobilní stanicí a jádrovou sítí"
---

DTAP je protokol jádrové sítě používaný pro transparentní přenos signalizačních zpráv nesouvisejících s hovorem, například zpráv správy mobility, mezi mobilní stanicí a jádrovou sítí.

## Popis

Direct Transfer Application Part (DTAP) je klíčový protokol v architektuře 3GPP, definovaný speciálně pro systémy GSM (2G) a UMTS (3G). Jeho hlavní funkcí je poskytovat transparentní transportní mechanismus pro signalizační zprávy nesouvisející s hovorem mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) či uživatelským zařízením (UE) a jádrovou sítí (CN). Tyto zprávy náleží do podsložek správy mobility ([MM](/mobilnisite/slovnik/mm/)) a správy spojení ([CM](/mobilnisite/slovnik/cm/)), které zahrnují procedury jako aktualizace polohy, autentizace, šifrování, řízení hovorů a správa doplňkových služeb. DTAP tyto zprávy neinterpretuje; funguje jako nosič, který zajišťuje jejich nezměněné doručení mezi MS/UE a entitami jádrové sítě, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN).

Z architektonického hlediska DTAP funguje v řídicí rovině rádiového rozhraní. V GSM jsou zprávy DTAP zapouzdřeny v protokolu Base Station System Application Part ([BSSAP](/mobilnisite/slovnik/bssap/)) pro přenos mezi Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) a MSC. BSSAP se dělí na dvě části: [BSS](/mobilnisite/slovnik/bss/) Management Application Part (BSSMAP) pro zprávy mezi BSC a MSC, které vyžadují interpretaci rádiovou sítí, a DTAP pro zprávy, které jsou pouze přeposílány. Podobně v UMTS jsou zprávy DTAP přenášeny v protokolu Radio Access Network Application Part (RANAP) mezi Radio Network Controller (RNC) a CN. Toto zapouzdření umožňuje rádiovému přístupovému systému (RAN) zpracovávat signalizaci specifickou pro rádiové rozhraní (pomocí BSSMAP nebo RANAP) odděleně od signalizace jádrové sítě (pomocí DTAP), čímž podporuje jasné funkční oddělení.

Fungování DTAP je poměrně přímočaré. Když MS vygeneruje zprávu MM nebo CM, je předána dolů v zásobníku protokolů a odeslána přes rozhraní vzduchu. Po přijetí BSC (GSM) nebo RNC (UMTS) identifikuje vrstva rádiové sítě zprávu jako zprávu DTAP na základě informačního prvku Discriminator. Uzel RAN následně zapouzdří tuto DTAP zprávu do zprávy BSSAP nebo RANAP DIRECT TRANSFER, která obsahuje potřebné identifikátory jako Connection Identifier (CI) nebo Iu Signaling Connection Identifier, a přepošle ji příslušnému uzlu CN. CN extrahuje DTAP zprávu a zpracuje obsaženou signalizaci MM nebo CM. Opačná coda funguje stejně pro zprávy z CN do MS. Tato transparentnost je klíčová, protože umožňuje protokolům jádrové sítě se vyvíjet nezávisle na technologii rádiového přístupu.

Role DTAP je zásadní pro škálovatelnost a udržovatelnost sítí 2G a 3G. Definováním čistého rozhraní mezi RAN a CN umožňuje efektivní interoperabilitu síťových zařízení od různých dodavatelů. RAN je odpovědný pouze za spolehlivý transport a signalizaci související s rádiovými zdroji, zatímco CN se stará o mobilitu účastníka, správu relací a služby. Toto oddělení odpovědností zjednodušuje síťovou architekturu, řešení problémů a zavádění nových služeb jádrové sítě bez nutnosti změn v prvcích rádiové sítě, pokud je podporován transparentní transportní mechanismus DTAP.

## K čemu slouží

DTAP byl vytvořen k řešení základního architektonického požadavku v celulárních sítích: jasného oddělení signalizačních odpovědností mezi rádiovým přístupovým systémem (RAN) a jádrovou sítí (CN). Před jeho formalizací v normách jako GSM bylo zpracování signalizace často více integrované, což mohlo vést ke složitým, na dodavateli závislým implementacím, které bránily interoperabilitě a vývoji sítě. Hlavní problém, který DTAP řeší, je umožnění transparentního průchodu signalizací specifickou pro účastníka a služby (jako je navázání hovoru nebo aktualizace polohy) přes síťové prvky (BSC, RNC), které by tuto informaci neměly potřebovat interpretovat nebo zpracovávat.

Jeho vytvoření bylo motivováno potřebou standardizované, škálovatelné architektury pro veřejné pozemní mobilní sítě. Definováním DTAP jako součásti protokolů BSSAP a později RANAP stanovila 3GPP model, ve kterém je role RAN omezena na správu rádiových zdrojů a mobility na úrovni buňky, zatímco CN spravuje identitu účastníka, mobilitu napříč většími oblastmi a servisní logiku. Toto oddělení umožňuje operátorům pořizovat zařízení RAN a CN od různých dodavatelů, což podporuje konkurenci a inovace. Také zajišťuje dlouhodobou životnost sítě, protože nové služby jádrové sítě lze zavádět aktualizací uzlů CN bez nutnosti úprav každého řadiče základnových stanic v terénu, pokud transportní kanál DTAP zůstává funkční.

Historicky je DTAP jedním ze základních kamenů úspěchu systému GSM a byl přenesen do UMTS. Odstranil omezení monolitičtějších architektur tím, že poskytl čisté, na zprávách založené rozhraní. Tento konstrukční princip oddělení transportu od zpracování zanechal trvalý odkaz v telekomunikacích a ovlivnil pozdější architektury, jako je oddělení řídicí a uživatelské roviny v 4G a 5G, ačkoli samotný protokol DTAP byl v těchto generacích nahrazen novými protokoly (jako S1-AP a NG-AP).

## Klíčové vlastnosti

- Transparentní transport signalizačních zpráv správy mobility (MM) a správy spojení (CM)
- Funguje jako podsložka v protokolech BSSAP (GSM) a RANAP (UMTS)
- Umožňuje jasné funkční oddělení odpovědností mezi rádiovým přístupovým systémem (RAN) a jádrovou sítí (CN)
- Používá informační prvek Discriminator k identifikaci typů zpráv pro správné směrování
- Spoléhá se na signalizační spojení na úrovni RAN (např. Iu Signaling Connection) pro spolehlivé doručení
- Podporuje všechny procedury nesouvisející s hovorem, jako je aktualizace polohy, autentizace a přenos SMS

## Související pojmy

- [BSSAP – Base Station Subsystem Application Part](/mobilnisite/slovnik/bssap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 49.008** (Rel-19) — BSSAP on E-interface for inter-MSC handover

---

📖 **Anglický originál a plná specifikace:** [DTAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtap/)
