---
slug: "neaf"
url: "/mobilnisite/slovnik/neaf/"
type: "slovnik"
title: "NEAF – Non-EPS Alert Flag"
date: 2025-01-01
abbr: "NEAF"
fullName: "Non-EPS Alert Flag"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/neaf/"
summary: "Příznak používaný v 4G Evolved Packet System (EPS) k označení, že uživatel, který momentálně není dosažitelný v EPS, může být dosažitelný přes službu mimo EPS (jako jsou 2G/3G sítě s přepojováním okru"
---

NEAF je příznak v 4G EPS, který indikuje, že uživatel nedosažitelný přes 4G může být dosažitelný přes službu mimo EPS, jako je 2G/3G, a spouští pokusy o alternativní doručení.

## Popis

Non-EPS Alert Flag (NEAF, příznak upozornění pro služby mimo EPS) je parametr používaný v rámci 4G Evolved Packet Core (EPC), konkrétně v kontextu Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)). Jedná se o booleovský indikátor uložený v MME pro uživatele. Příznak je nastaven, když MME obdrží indikaci, že User Equipment (UE) není dosažitelné pro služby EPS (např. kvůli absenci pokrytí LTE nebo kvůli úspornému režimu jako Extended Idle Mode [DRX](/mobilnisite/slovnik/drx/)), ale existuje možnost, že je UE připojeno ke službě mimo EPS. Služby mimo EPS primárně odkazují na služby s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) poskytované 2G ([GERAN](/mobilnisite/slovnik/geran/)) nebo 3G (UTRAN) rádiovými přístupovými sítěmi. Příznak se používá ve spojení s rozhraním SGs, které propojuje MME (EPS) se serverem Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) (CS doména). Když pro UE dorazí na MSC událost iniciovaná sítí (jako SMS nebo CS hlasový hovor) a MME indikuje, že UE je odpojeno od EPS, ale NEAF je nastaven, je MSC informováno, že by měl být spuštěn mechanismus upozornění. To typicky spustí, aby MSC provedlo paging UE v CS doméně. Primární aplikací NEAF je doručování SMS přes SGs (SMS in MME) a procedury CS Fallback ([CSFB](/mobilnisite/slovnik/csfb/)). Když MME obdrží přes rozhraní SGs od MSC oznámení o příchozí CS službě, zkontroluje kontext správy mobility UE. Pokud je UE označeno jako nedosažitelné pro EPS, ale NEAF má hodnotu TRUE, MME přijme požadavek na službu a zahájí procedury (jako paging v CS doméně) k upozornění UE. Tento mechanismus zajišťuje, že služby jako SMS a hlasové hovory mohou být stále doručeny k UE, které je dočasně mimo pokrytí LTE, ale je registrované v 2G/3G síti.

## K čemu slouží

NEAF byl vytvořen, aby překlenul mezeru v kontinuitě služeb mezi plně IP 4G EPS a staršími sítěmi s přepojováním okruhů během přechodové fáze mobilních sítí. Řeší problém, kdy je UE nedosažitelné pro služby EPS (jako SMS přes IMS nebo VoLTE), ale potenciálně dosažitelné přes starší [CS](/mobilnisite/slovnik/cs/) síť. Bez tohoto příznaku by síť mohla UE jednoduše považovat za zcela nedosažitelné, což by vedlo ke ztraceným SMS zprávám nebo neúspěšným pokusům o sestavení hovoru, když je UE připojeno k 2G/3G. Jeho zavedení, zejména s rozhraním SGs ve verzi 8, bylo motivováno potřebou podpory SMS a CS Fallback pro hlasové hovory v raných nasazeních LTE, která často postrádala plné pokrytí hlasovými službami založenými na IMS (VoLTE). Řešil omezení čistého EPS, které původně nemělo nativní funkcionalitu pro přepojování okruhů, tím, že poskytl signalizační mechanismus pro využití všudypřítomného CS jádra pro základní služby, dokud se služby IMS nerozšířily. To umožnilo operátorům zavádět LTE datové služby při zachování spolehlivé podpory pro všudypřítomné služby jako SMS a hlas s přepojováním okruhů.

## Klíčové vlastnosti

- Booleovský příznak uložený v kontextu správy mobility MME pro účastníka
- Indikuje potenciální dosažitelnost UE v sítích mimo EPS (2G/3G CS), když selže dosažitelnost v EPS
- Klíčový prvek pro doručování SMS přes rozhraní SGs (SMS in MME)
- Používá se v procedurách CS Fallback (CSFB) pro příchozí hlasové hovory
- Funguje ve spojení s rozhraním SGs mezi MME a serverem MSC
- Pomáhá udržovat kontinuitu služeb mezi doménami EPS a staršími CS doménami

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [EPS – Evolved Packet System](/mobilnisite/slovnik/eps/)

## Definující specifikace

- **TS 29.118** (Rel-19) — MME-VLR Interface for CS Fallback & SMS

---

📖 **Anglický originál a plná specifikace:** [NEAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/neaf/)
