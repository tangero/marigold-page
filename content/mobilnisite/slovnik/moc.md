---
slug: "moc"
url: "/mobilnisite/slovnik/moc/"
type: "slovnik"
title: "MOC – Mobile Originated Call (attempt)"
date: 2026-01-01
abbr: "MOC"
fullName: "Mobile Originated Call (attempt)"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/moc/"
summary: "Mobile Originated Call (MOC) označuje pokus o hovor iniciovaný mobilním účastníkem. Jde o základní služební metriku v telekomunikacích, která představuje zahájení hlasové relace ze strany uživatelskéh"
---

MOC (Mobile Originated Call) je pokus o hovor iniciovaný mobilním účastníkem, používaný jako klíčový ukazatel výkonnosti v 3GPP pro testování, monitorování a účtování za účelem posouzení dostupnosti sítě.

## Popis

Pokus o Mobile Originated Call (MOC) je procesní zahájení hlasového hovoru mobilním uživatelským zařízením (UE). Představuje okamžik, kdy účastník vytočí číslo a stiskne tlačítko pro volání, čímž spustí řadu síťových signalizačních procedur. Z technického hlediska začíná pokus o MOC odesláním žádosti o službu (např. Extended Service Request pro [CS](/mobilnisite/slovnik/cs/) fallback nebo [SIP](/mobilnisite/slovnik/sip/) INVITE pro VoLTE/VoNR) ze strany UE do sítě, která žádá o prostředky pro vytvoření hlasového přenosu. Proces zahrnuje všechny kroky od počátečního přístupu až po okamžik, kdy je na straně volaného indikováno vyzvánění (ringing), nebo dokud se pokus nezdaří.

Architektura podílející se na zpracování MOC zahrnuje více síťových domén. V samostatné 5G síti ([SA](/mobilnisite/slovnik/sa/)) využívající Voice over New Radio (VoNR) UE iniciuje žádost o modifikaci [PDU](/mobilnisite/slovnik/pdu/) relace pro IMS hlasový přenos. Funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) ve spolupráci s funkcí řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) zřídí příslušné QoS toky. IMS core následně zpracovává SIP signalizaci. Ve scénářích 4G LTE nebo nesamostatné 5G sítě ([NSA](/mobilnisite/slovnik/nsa/)) využívajících VoLTE nebo Circuit-Switched Fallback ([CSFB](/mobilnisite/slovnik/csfb/)) spouští MOC odlišné procedury zahrnující MME, MSC Server nebo IMS. Mezi klíčové síťové komponenty patří UE (iniciátor), RAN (gNB/eNB), funkce řídicí roviny jádra (AMF/MME, SMF), IMS core (P-CSCF, S-CSCF) a případně Media Gateway.

MOC není jen uživatelská akce, ale kritická měřitelná událost. Ve specifikacích 3GPP, zejména od Technické specifikační skupiny pro služby a aspekty systémů (TSG SA) a TSG Core Network and Terminals (TSG CT), se pokusy o MOC používají k definování testovacích případů pro konformitu síťových zařízení a UE. Jsou také zásadní pro standardy správy výkonnosti (PM) a správy poruch (FM), kde čítače úspěšnosti a neúspěšnosti pokusů o MOC představují klíčové ukazatele výkonnosti (KPI) pro operátory monitorující stav služeb a jejich dostupnost. Dále jsou na základě úspěšných událostí MOC generovány záznamy o účtování (CDR), které tvoří podklad pro fakturaci.

## K čemu slouží

Koncept pokusu o Mobile Originated Call existuje jako základní, atomická měrná jednotka pro službu hlasové telefonie v mobilních sítích. Slouží několika klíčovým účelům: definici testovacích procedur, umožnění monitorování výkonnosti a usnadnění přesného účtování. Bez standardizované definice toho, co představuje pokus o hovor a jaké jsou jeho počáteční a koncové body, by nebylo možné konzistentně měřit úspěšnost sestavení hovoru (primární metrika kvality sítě) ani generovat srovnatelné účtovací záznamy napříč různými síťovými dodavateli a operátory.

Historicky, v čistě okruhově spínaných sítích (2G/3G), byl pokus o MOC jasně definován iniciací zprávy pro sestavení hovoru na rádiovém kanálu. S evolucí na paketově spínaný hlas (VoIP přes IMS) bylo nutné definici přizpůsobit novému signalizačnímu paradigmatu (SIP), ale základní potřeba zůstala. Specifikace 3GPP pečlivě definují proceduru MOC napříč všemi generacemi a hlasovými řešeními (CS, VoLTE, VoNR, CSFB), aby zajistily konzistenci. To umožňuje operátorům porovnávat výkonnost, technikům diagnostikovat problémy za použití společného terminologického rámce a fakturačním systémům správně aplikovat tarify na základě vyvolání služby. Odstraňuje tak omezení plynoucí z interpretace 'pokusu o hovor' specifické pro konkrétního dodavatele nebo implementaci, což by bránilo interoperabilitě, roamingu a spravedlivému účtování.

## Klíčové vlastnosti

- Představuje zahájení hlasového hovoru mobilním UE.
- Spouští signalizaci v jádru sítě pro vytvoření přenosu (CS nebo PS).
- Slouží jako základní událost pro měření výkonnosti sítě (KPI).
- Používá se jako podklad pro generování záznamů o účtování (CDR).
- Definován v testovacích případech pro konformitu UE a síťových zařízení.
- Aplikovatelný napříč více technologiemi (CS, VoLTE, VoNR, CSFB).

## Definující specifikace

- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.629** (Rel-19) — SON Policy NRM IRP Solution Set Definitions
- **TS 28.632** (Rel-19) — Inventory Management NRM Integration Reference Point
- **TS 28.653** (Rel-19) — UTRAN NRM IRP Solution Set Definition
- **TS 28.656** (Rel-19) — GERAN NRM IRP Solution Set Definitions
- **TS 28.659** (Rel-19) — E-UTRAN NRM IRP Solution Set Definitions
- **TS 28.663** (Rel-19) — Generic RAN NRM IRP Solution Set Definitions
- **TS 28.673** (Rel-19) — HNS NRM IRP Solution Set Definitions
- **TS 28.676** (Rel-19) — HeNS NRM IRP Solution Set Definitions
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 28.703** (Rel-19) — Core Network NRM IRP Solution Set Definitions
- **TS 28.706** (Rel-19) — IMS NRM IRP Solution Set definitions
- **TS 28.707** (Rel-19) — EPC NRM IRP Requirements
- … a dalších 77 specifikací

---

📖 **Anglický originál a plná specifikace:** [MOC na 3GPP Explorer](https://3gpp-explorer.com/glossary/moc/)
