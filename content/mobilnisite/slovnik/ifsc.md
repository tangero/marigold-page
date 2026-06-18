---
slug: "ifsc"
url: "/mobilnisite/slovnik/ifsc/"
type: "slovnik"
title: "IFSC – Information Field Size for the UICC"
date: 2025-01-01
abbr: "IFSC"
fullName: "Information Field Size for the UICC"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ifsc/"
summary: "Podmnožina velikostí informačních polí (Information Field Sizes), která konkrétně definuje maximální délky datových polí používaných v komunikaci s univerzální integrovanou obvodovou kartou (UICC), vč"
---

IFSC je standardizovaná maximální délka datového pole používaná v komunikaci mezi mobilním terminálem a UICC (např. SIM kartou) pro zabezpečenou autentizaci, správu předplatného a aplikační příkazy.

## Popis

Velikost informačního pole pro UICC (IFSC) je specializovaná specifikace v rámci standardů 3GPP, která určuje maximální bitové nebo bajtové délky pro datová pole vyměňovaná mezi mobilním zařízením ([ME](/mobilnisite/slovnik/me/)) a univerzální integrovanou obvodovou kartou (UICC), která obsahuje aplikaci modulu identifikace účastníka ([SIM](/mobilnisite/slovnik/sim/)) nebo univerzálního modulu identifikace účastníka ([USIM](/mobilnisite/slovnik/usim/)). Tyto velikosti jsou definovány ve specifikacích jako TS 21.905 a jsou klíčové pro přesnou funkci rozhraní (elektrického a logického spojení) definovaného standardy [ETSI](/mobilnisite/slovnik/etsi/)/3GPP, například TS 31.101. IFSC řídí pole v aplikačních protokolových datových jednotkách ([APDU](/mobilnisite/slovnik/apdu/)), což jsou pakety příkaz-odpověď používané pro veškerou interakci s UICC. To zahrnuje příkazy pro přístup k souborům, výzvy a odpovědi autentizačních procedur (pomocí algoritmů MILENAGE nebo TUAK), správu profilů a SIM Application Toolkit ([SAT](/mobilnisite/slovnik/sat/)/[USAT](/mobilnisite/slovnik/usat/)).

Z architektonického hlediska IFSC zajišťuje, že terminál (vrstva rozhraní UICC v ME) a samotná UICC jsou ve shodě ohledně struktury každé zprávy. Například definuje maximální velikost pro [RAND](/mobilnisite/slovnik/rand/) (náhodnou výzvu) používanou při autentizaci, délku šifrovacího klíče (CK) a integritního klíče (IK) nebo velikost obálky příkazu pro stahování SMS-PP. Když ME odešle příkazový APDU do UICC, musí každé datové pole naformátovat v souladu s IFSC. UICC po přijetí analyzuje příkaz na základě těchto stejných definic velikostí, zpracuje jej (např. vypočítá autentizační odpověď SRES) a vrátí odpověď APDU, jejíž pole také odpovídají IFSC. Tato přesná velikost je zásadní pro správnou funkci nízkorozměrových komunikačních protokolů T=0 nebo T=1 a pro bezpečnostní algoritmy, které závisí na vstupech pevné délky.

Role IFSC je prvořadá pro zabezpečení a interoperabilitu. Standardizací velikostí citlivých polí, jako jsou kryptografické klíče a autentizační parametry, zabraňuje útokům přetečení bufferu a zajišťuje, že se bezpečnostní výpočty provádějí nad daty správné velikosti. Také umožňuje, aby UICC od jednoho výrobce bezproblémově fungovaly v mobilních zařízeních od jakéhokoli jiného výrobce. Dále, jak se schopnosti UICC rozvíjely pro podporu větších telefonních seznamů, více aplikací a dálkové provizionování vestavěných SIM (eSIM), byly definice IFSC aktualizovány, aby pojmuly větší identifikátory souborů a datové objekty. V kontextu eSIM a architektury dálkového provizionování SIM (RSP) je IFSC pro příkazy související se stažením a správou profilů (prostřednictvím SM-DP+ a SM-DS) klíčová pro zabezpečené a spolehlivé aktualizace přes vzdušné rozhraní. IFSC tedy tvoří nepříliš zmiňovaná, ale zásadní gramatická pravidla pro bezpečný dialog mezi telefonem a jeho čipovou kartou.

## K čemu slouží

IFSC bylo vytvořeno, aby řešilo konkrétní potřebu spolehlivé a bezpečné komunikace mezi mobilním terminálem a výměnnou čipovou kartou (UICC). V raných systémech GSM, bez standardizovaných velikostí polí pro SIM příkazy, mohly vznikat problémy s interoperabilitou vedoucí k neúspěšné autentizaci, poškozeným položkám telefonního seznamu nebo dokonce zablokování karty. Definice IFSC poskytla pro toto kritické rozhraní striktní smlouvu, která zajistila, že všechny výrobci telefonů a SIM karet mohou komunikovat předvídatelně. To bylo zásadní pro celosvětový ekosystém roamingu, kde musí SIM karta účastníka fungovat v jakémkoli kompatibilním telefonu na světě.

Hlavními problémy, které IFSC řeší, jsou integrita dat a zajištění zabezpečení v dialogu ME-UICC. Pevným stanovením velikostí polí používaných v autentizačních vektorech a generování klíčů odstraňuje nejednoznačnosti, které by mohly oslabit kryptografické operace. Také umožňuje efektivní implementaci softwaru pro zpracování APDU jak v základnovém procesoru terminálu, tak v operačním systému UICC. Jak se služby uložené na UICC stávaly složitějšími (od jednoduchých telefonních seznamů na SIM po javové aplety a síťovou autentizaci pro 3G/4G/5G), definice IFSC se vyvíjely, aby podporovaly větší datové objekty a nové sady příkazů, což umožnilo tento inovační vývoj bez narušení stávající funkčnosti. IFSC je základním kamenem důvěryhodného, na hardwaru založeného bezpečnostního základu, který podpírá identitu účastníka a přenositelnost služeb v mobilních sítích.

## Klíčové vlastnosti

- Definuje maximální velikosti pro datová pole v příkazech APDU z ME do UICC (SIM/USIM)
- Zajišťuje interoperabilitu mezi jakýmkoli mobilním zařízením a jakoukoli UICC/SIM kartou
- Klíčová pro správnou funkci autentizačních procedur a procedur dohodnutí klíče
- Podporuje příkazy pro přístup k souborům, aplikační toolkit a dálkové provizionování
- Poskytuje základ pro komunikaci se zabezpečeným prvkem a integritu dat
- Vyvíjí se, aby podporovala nové aplikace UICC a schopnosti eSIM

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [APDU – Application Protocol Data Unit](/mobilnisite/slovnik/apdu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [IFSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ifsc/)
