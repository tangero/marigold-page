---
slug: "ulr"
url: "/mobilnisite/slovnik/ulr/"
type: "slovnik"
title: "ULR – Update Location Request"
date: 2026-01-01
abbr: "ULR"
fullName: "Update Location Request"
category: "Core Network"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ulr/"
summary: "ULR je příkaz Diameter používaný v síti 5G jádra (5GC) mezi funkcí pro správu přístupu a mobility (AMF) a jednotnou správou dat (UDM). Odesílá se k registraci aktuální polohy UE, získání předplatitels"
---

ULR je příkaz Diameter odeslaný z AMF do UDM v síti 5G jádra za účelem registrace polohy UE, získání jeho předplatitelských dat a autentizace uživatele.

## Popis

Update Location Request (ULR) je klíčová příkazová zpráva založená na protokolu Diameter, definovaná v 3GPP TS 29.272 a TS 33.501 pro 5G systém (5GS). Používá se na rozhraní N8 (v 5G) mezi funkcí pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a jednotnou správou dat ([UDM](/mobilnisite/slovnik/udm/)). Primární funkcí příkazu ULR je informovat UDM o aktuální obslužném síťovém uzlu (AMF) pro UE a vyžádat si předplatitelský profil a autentizační data UE. Tento postup je ústřední pro počáteční registraci, aktualizace registrace při mobilitě a periodické registrační procesy v 5G.

Z architektonického hlediska AMF funguje jako klient Diameter, který iniciuje příkaz ULR směrem k UDM, jež funguje jako server Diameter. Zpráva obsahuje množství informací ve svých párech atribut-hodnota ([AVP](/mobilnisite/slovnik/avp/)). Mezi klíčové AVP patří User-Name (obsahující [SUPI](/mobilnisite/slovnik/supi/) nebo [SUCI](/mobilnisite/slovnik/suci/)), Visited-PLMN-Id, RAT-Type (např. NR, [E-UTRA](/mobilnisite/slovnik/e-utra/)) a identita AMF. Po přijetí ULR UDM žádost ověří, zkontroluje stav předplatitele a může spustit autentizační procedury s funkcí autentizačního serveru ([AUSF](/mobilnisite/slovnik/ausf/)).

Jeho fungování je integrováno do toku registrace UE. Když se UE pokouší zaregistrovat v síti 5G, AMF po počáteční interakci s UE odešle příkaz ULR do UDM. UDM tento požadavek zpracuje: autentizuje předplatitele, autorizuje registraci pro danou [PLMN](/mobilnisite/slovnik/plmn/) a typ přístupu a načte profil předplatitele ze své databáze. UDM poté odpoví příkazem Update Location Answer (ULA). Příkaz ULA přenáší zpět k AMF klíčová data, včetně předplatitelských dat pro přístup a mobilitu, dat pro správu relací a potenciálně autentizačních vektorů.

Jeho role je zásadní pro mobilitu, zabezpečení a vynucování politik. Výměna ULR/ULA zajišťuje, že UDM jako centrální úložiště předplatitelských dat má vždy přehled o obslužné AMF pro dané UE. To umožňuje funkce jako zákonné odposlechy, omezení služeb na základě předplatného a notifikace o událostech mobility pro ostatní síťové funkce (NF). Nahrazuje proceduru Update Location Request používanou na rozhraní S6a/S6d založeném na Diameter mezi MME a HSS v 4G EPS, upravenou pro servisně orientovanou architekturu 5GC.

## K čemu slouží

Příkaz ULR existuje, aby poskytl standardizovaný, bezpečný a efektivní mechanismus pro aktualizaci polohy a získání předplatitelských dat v servisně orientované síti 5G jádra. Řeší potřebu odděleného, škálovatelného postupu v nové cloud-nativní architektuře, která se odklání od point-to-point rozhraní GTP a Diameter předchozích generací. V 4G EPS existoval podobný Update Location Request na rozhraní S6a mezi MME a HSS, ale 5G ULR je přizpůsoben novým síťovým funkcím (AMF/UDM) a podporuje vylepšené bezpečnostní funkce, jako je skrytí identifikace předplatitele (SUCI).

Problém, který řeší, je udržování přesné a včasné znalosti o připojovacím bodě předplatitele v síti pro správu mobility, poskytování služeb a regulatorní shodu. Bez tohoto postupu by síť jádra nevěděla, která AMF obsluhuje dané UE, což by znemožnilo směrování mobilně-terminovaných relací, aplikování správných mobilních politik nebo zajištění, že je předplatitel oprávněn síť používat. Je to primární spouštěč pro UDM, aby poskytlo AMF profil služeb předplatitele.

Jeho vytvoření bylo dále motivováno 5G designovými principy síťového řezání, bezstavových NF a servisně orientovaných interakcí. Procedura ULR, používající HTTP/2 s JSON nebo Diameter přes SBA, umožňuje AMF přihlásit se k odběru změn v datech UDM, což ve srovnání se statickým modelem "pull" umožňuje dynamičtější a efektivnější aktualizace, a tím podporuje pokročilé use case jako síťové řezy a edge computing.

## Klíčové vlastnosti

- Příkaz Diameter (nebo servisní operace HTTP/2) pro komunikaci AMF-UDM
- Spouští autentizaci a autorizaci předplatitele během registrace
- Přenáší SUPI/SUCI UE a identitu obslužné sítě/AMF
- Získává předplatitelská data pro přístup a mobilitu a pro správu relací
- Podporuje síťové řezy přenosem informací S-NSSAI
- Umožňuje UDM udržovat mapování SUPI na obslužnou AMF pro mobilně-terminované služby

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [ULR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ulr/)
