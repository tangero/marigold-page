---
slug: "sufi"
url: "/mobilnisite/slovnik/sufi/"
type: "slovnik"
title: "SUFI – SUper FIeld"
date: 2025-01-01
abbr: "SUFI"
fullName: "SUper FIeld"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sufi/"
summary: "SUFI je proměnně dlouhé řídicí pole používané ve vrstvě protokolu řízení rádiového spoje (Radio Link Control, RLC) v 3GPP UMTS. Nese stavové informace, primárně pro potvrzovaný režim (Acknowledged Mod"
---

SUFI je proměnně dlouhé řídicí pole používané ve vrstvě protokolu RLC v 3GPP UMTS pro přenos stavových informací za účelem usnadnění selektivních retransmisí v potvrzovaném režimu (Acknowledged Mode).

## Popis

SUper FIeld (SUFI) je základním prvkem protokolu řízení rádiového spoje (Radio Link Control, [RLC](/mobilnisite/slovnik/rlc/)), specifikovaného pro UMTS od 3GPP Release 4 a novějších. Operuje uvnitř řídicí protokolové datové jednotky (Protocol Data Unit, [PDU](/mobilnisite/slovnik/pdu/)) RLC. SUFI není pole s pevným formátem; jedná se spíše o strukturu podobnou [TLV](/mobilnisite/slovnik/tlv/) (Type-Length-Value), používanou k přenosu specifických řídicích informací mezi partnerskými entitami RLC, primárně v potvrzovaném režimu (Acknowledged Mode, [AM](/mobilnisite/slovnik/am/)). Vysílající entita RLC zahrnuje SUFI do svých řídicích PDU, aby signalizovala přijímači události jako potvrzení, aktualizace okna nebo chybové stavy, a naopak.

SUFI se skládá ze tří hlavních částí: typu SUFI (SUFI Type), délky SUFI (SUFI Length) a dat SUFI (SUFI Data nebo Value). Typ SUFI je krátký identifikátor, který definuje význam a formát následujících dat (např. [ACK](/mobilnisite/slovnik/ack/), LIST, BITMAP, WINDOW). Délka SUFI udává velikost pole dat SUFI v oktetech. Data SUFI obsahují samotné řídicí informace, jejichž interpretace zcela závisí na typu SUFI. Například SUFI typu 'ACK' obsahuje číslo sekvence potvrzující přijetí všech PDU až do tohoto bodu, zatímco SUFI typu 'LIST' obsahuje seznam specifických čísel sekvencí, která jsou potvrzována nebo nahlášena jako chybějící. SUFI typu 'WINDOW' se používá k oznámení aktuální velikosti přijímacího okna.

Fungování SUFI je klíčové pro [ARQ](/mobilnisite/slovnik/arq/) mechanismus RLC AM. Když přijímač RLC AM detekuje chybějící PDU (mezery v prostoru čísel sekvence), může vygenerovat STATUS PDU obsahující jedno nebo více SUFI (jako LIST nebo BITMAP), aby přesně informoval vysílač o tom, která PDU je potřeba retransmitovat. To umožňuje selektivní opakování ARQ, které je efektivnější než metoda go-back-N. Vysílač zpracuje přijatá SUFI, aktualizuje stav své vysílací fronty a podle toho naplánuje retransmise. SUFI se také používají pro obnovu po chybě protokolu a resetovací procedury. Jejich proměnně dlouhý, typem řízený návrh činí řídicí protokol RLC flexibilním a efektivním, protože je potřeba přenášet pouze informace nezbytné pro danou situaci, čímž se šetří cenné rádiové prostředky.

## K čemu slouží

SUFI bylo vytvořeno, aby poskytlo flexibilní a efektivní signalizační mechanismus pro řídicí rovinu vrstvy [RLC](/mobilnisite/slovnik/rlc/) v UMTS. Před UMTS měly systémy 2G, jako je GSM, jednodušší linkové protokoly. Zavedení UMTS s jeho širším spektrem služeb (od hlasu po paketová data) a náročnějšími rádiovými podmínkami vyžadovalo robustní a efektivní [ARQ](/mobilnisite/slovnik/arq/) mechanismus na vrstvě 2 (Layer 2) pro zajištění spolehlivého přenosu dat. Potvrzovaný režim RLC potřeboval způsob výměny komplexních stavových informací – jako je potvrzení rozsahu rámců, nahlášení seznamu chybějících rámců nebo správa přijímacího okna – bez definice množství řídicích zpráv s pevným formátem.

Koncept SUFI to vyřešil zavedením obecného, rozšiřitelného kontejneru pro řídicí informace. Tento návrh odstranil omezení plynoucí z pevné sady typů řídicích PDU, které by byly buď příliš zjednodušené, nebo plýtvavé. S SUFI může jediný formát STATUS PDU nést jakoukoli kombinaci potřebných řídicích informací zřetězením různých prvků SUFI. Například může nést ACK pro rozsah, LIST pro specifická chybějící PDU a aktualizaci WINDOW, vše v jedné efektivně zakódované PDU. Tato flexibilita byla klíčová pro optimalizaci výkonu přes proměnlivé a náchylné k chybám WCDMA rádiové rozhraní.

SUFI navíc umožnily protokolu RLC přizpůsobit se různým vzorcům datového toku. Pro kontinuální streamování s málo chybami postačí jednoduchá SUFI typu ACK. Pro chyby v dávkách umožňují podrobná SUFI typu LIST nebo BITMAP přesné žádosti o retransmisi. Tato efektivita v řídicí signalizaci přímo přispívá k vyšší propustnosti uživatelských dat a nižší latenci, což byly klíčové cíle pro paketové služby UMTS. Mechanismus SUFI vytvořil vzor návrhu pro flexibilní řízení na vrstvě 2, který ovlivnil pozdější 3GPP systémy, i když se konkrétní protokol RLC vyvíjel v LTE a 5G NR.

## Klíčové vlastnosti

- Proměnně dlouhý řídicí informační prvek ve stylu TLV
- Definován identifikátorem typu, který diktuje formát dat
- Přenášen uvnitř řídicích PDU RLC (STATUS PDU)
- Umožňuje selektivní opakování ARQ s přesným potvrzením/negativním potvrzením
- Podporuje různé řídicí funkce: ACK, LIST, BITMAP, WINDOW atd.
- Flexibilní zřetězení více SUFI v jedné řídicí PDU

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 25.322** (Rel-19) — RLC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SUFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sufi/)
