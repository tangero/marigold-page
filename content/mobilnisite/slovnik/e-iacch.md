---
slug: "e-iacch"
url: "/mobilnisite/slovnik/e-iacch/"
type: "slovnik"
title: "E-IACCH – Enhanced Inband Associated Control CHannel"
date: 2025-01-01
abbr: "E-IACCH"
fullName: "Enhanced Inband Associated Control CHannel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-iacch/"
summary: "Řídicí kanál v GSM/EDGE sítích, který přenáší signalizační informace v pásmu společně s kanálem pro přenos dat (traffic channel). Zvyšuje spolehlivost a kapacitu pro řídicí signalizaci, která je klíčo"
---

E-IACCH je rozšířený přidružený řídicí kanál v pásmu (Enhanced Inband Associated Control CHannel) v GSM/EDGE sítích, který přenáší signalizaci pro zřízení hovoru, přepojení a služby, zvyšující jeho spolehlivost a kapacitu.

## Popis

Rozšířený přidružený řídicí kanál v pásmu (Enhanced Inband Associated Control CHannel, E-IACCH) je základní signalizační kanál v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)). Funguje multiplexováním řídicích signalizačních informací přímo na stejný fyzický zdroj jako kanál pro přenos dat uživatele ([TCH](/mobilnisite/slovnik/tch/)), konkrétně struktury Pomale přidruženého řídicího kanálu ([SACCH](/mobilnisite/slovnik/sacch/)) a Rychle přidruženého řídicího kanálu ([FACCH](/mobilnisite/slovnik/facch/)). Tento přístup v pásmu je efektivní, protože využívá přidělené spektrum pro hovor také k řízení řídicí roviny hovoru, což eliminuje potřebu samostatných vyhrazených signalizačních zdrojů pro každé aktivní spojení. Kanál přenáší kritické signalizační zprávy Layer 2 a Layer 3, včetně měřených reportů, příkazů přepojení, instrukcí řízení výkonu a správy šifrovacího módu.

Architektonicky je E-IACCH implementován v základní přenosové stanici ([BTS](/mobilnisite/slovnik/bts/)) a mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). Funguje tak, že "krade" bursty z kanálu pro přenos dat k vysílání řídicích informací. Když je potřebná urgentní signalizace (např. pro přepojení), systém využívá FACCH, který nahradí celý rámec přenosu dat signalizačními daty, což poskytuje rychlou, ale rušivou signalizaci. Pro méně časově kritickou periodickou signalizaci (např. měření kvality spojení) je využíván SACCH, který přiděluje specifické časové sloty ve strukture multiframe bez narušení rámců pro hovor. Část "Rozšířený" (Enhanced) se týká vylepšení kódování a robustnosti těchto přidružených řídicích kanálů, zaváděných v pozdějších fázích GSM.

Jeho role v síti je klíčová pro udržení integrity hovoru a umožnění mobility. Bez spolehlivého přenosu těchto řídicích zpráv by funkce jako přepojení mezi buňkami selhaly, vedoucí k přerušeným hovorům. E-IACCH zajišťuje, že síť může dynamicky řídit rádiový spoj, adaptovat se na změněné podmínky signálu a mobilitu uživatele, a tím poskytovat stabilní a kontinuální službu. Je klíčovou komponentou na rozhraní Um mezi MS a BTS, tvořící páteř signalizace rádiového rozhraní pro aktivní spojení.

## K čemu slouží

E-IACCH byl vytvořen k poskytnutí vyhrazené, spolehlivé a efektivní signalizační cesty pro aktivní kanál přenosu dat (traffic channel) v GSM sítích. Před jeho zavedením a rozšířením byla řídicí signalizace pro aktivní hovory méně robustní a mohla být limitujícím faktorem pro výkon síťě a spolehlivost služby. Primární problém, který řeší, je potřebnost přenášet kritické řídicí informace — jako příkazy přepojení, měřené reporty a změny šifrovacího módu — současně s uživatelským hovorovým nebo datovým přenosem bez potřebnosti samostatného, vyhrazeného rádiového kanálu pro každý hovor, což by bylo spektrálně neefektivní.

Historický kontext pochází z původních GSM specifikací, které definovaly přidružené řídicí kanály (ACCHs) jako část struktury [TDMA](/mobilnisite/slovnik/tdma/) frame. Vylepšení "Rozšířený" (Enhanced) bylo motivované potřebností větší signalizační kapacity a robustnosti, speciálně s zaváděním vyšších datových služeb jako EDGE. Rozšířené kódovací schémata a lepší využití "ukradených" burstů zvýšily spolehlivost signalizace v podmínkách slabého rádiového signálu, což je esenciální pro udržení kvality hovoru a úspěšné přepojení. Toto řešilo limity, kde signalizační chyby mohly direktně vést ke degradaci nebo přerušení služby.

## Klíčové vlastnosti

- Multiplexování v pásmu s kanálem přenosu dat (TCH)
- Podporuje rychlé (FACCH) i pomalé (SACCH) signalizační módy
- Přenáší kritické řídicí zprávy Layer 2 & Layer 3
- Umožňuje přepojení, řízení výkonu a správu šifrování
- Využívá "kradení" burstů pro urgentní signalizaci (FACCH)
- Poskytuje periodickou signalizaci na vyhrazených slotech (SACCH)

## Související pojmy

- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)
- [FACCH – Fast Associated Control CHannel](/mobilnisite/slovnik/facch/)
- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description

---

📖 **Anglický originál a plná specifikace:** [E-IACCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-iacch/)
