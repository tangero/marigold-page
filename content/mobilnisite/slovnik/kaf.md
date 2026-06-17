---
slug: "kaf"
url: "/mobilnisite/slovnik/kaf/"
type: "slovnik"
title: "KAF – AKMA Application Key"
date: 2025-01-01
abbr: "KAF"
fullName: "AKMA Application Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/kaf/"
summary: "Kryptografický klíč odvozený v rámci architektury AKMA pro zabezpečení komunikace na aplikační úrovni mezi UE a aplikační funkcí (AF). Umožňuje bezpečný přístup ke službám bez nutnosti nových autentiz"
---

KAF je kryptografický klíč odvozený v rámci architektury AKMA pro zabezpečení komunikace na aplikační úrovni mezi uživatelským zařízením (User Equipment, UE) a aplikační funkcí (Application Function, AF), což umožňuje efektivní a bezpečný přístup ke službám.

## Popis

KAF ([AKMA](/mobilnisite/slovnik/akma/) Application Key) je klíčový bezpečnostní prvek v rámci architektury Authentication and Key Management for Applications (AKMA) standardizované 3GPP. Jedná se o symetrický kryptografický klíč jednoznačně generovaný pro konkrétní uživatelské zařízení (UE) a konkrétní aplikační funkci ([AF](/mobilnisite/slovnik/af/)). KAF není přímo zřízen, ale je dynamicky odvozen z kořenového klíče známého jako [KAKMA](/mobilnisite/slovnik/kakma/) (AKMA Anchor Key), který je sám navázán během primární autentizační procedury 5G [AKA](/mobilnisite/slovnik/aka/) nebo EAP-AKA' mezi UE a sítí. Proces odvození zahrnuje vstupní parametry, jako je identita AF (např. její [FQDN](/mobilnisite/slovnik/fqdn/)), což zajišťuje oddělení klíčů tak, že každý pár UE-AF má odlišný KAF.

Generování KAF je distribuovaný proces. UE a funkce AKMA Anchor Function (AAnF) v domovské síti nezávisle vypočítají stejný KAF pomocí sdíleného KAKMA a dohodnutých vstupů pro odvození. AAnF pak tento KAF bezpečně poskytne žádající AF přes rozhraní Naf. Tato architektura zajišťuje, že AF se nikdy nedozví kořenový KAKMA a UE nikdy neposkytuje KAF navenek, čímž se udržuje silný bezpečnostní řetězec. Primární role KAF je umožnit navázání zabezpečeného kanálu, typicky pomocí TLS-PSK (Pre-Shared Key) nebo podobných mechanismů, mezi UE a AF.

Jakmile je navázán, KAF se používá k zabezpečení komunikace na aplikační vrstvě. Může přímo sloužit jako předem sdílený klíč (PSK) pro TLS nebo být použit k odvození dalších relací klíčů pro šifrování a ochranu integrity aplikačních dat. Tento model přesouvá autentizaci a správu klíčů z aplikačního serveru na bezpečnostní infrastrukturu 3GPP a využívá robustní, na předplatném založenou síťovou autentizaci. Životní cyklus KAF je svázán se základním KAKMA; zůstává platný, dokud je platný KAKMA, což je obvykle sladěno s registračním stavem UE, což poskytuje rovnováhu mezi bezpečností a kontinuitou služeb.

## K čemu slouží

KAF byl zaveden, aby vyřešil problém opakované a neefektivní autentizace pro over-the-top ([OTT](/mobilnisite/slovnik/ott/)) a operátorem hostované aplikace přistupující k sítím 3GPP. Před [AKMA](/mobilnisite/slovnik/akma/) často aplikace vyžadovaly vlastní autentizační mechanismy (jako uživatelská jména/hesla nebo [API](/mobilnisite/slovnik/api/) tokeny), které byly oddělené od robustní autentizace v mobilní síti. To vedlo ke špatné uživatelské zkušenosti, zvyšovalo režii správy přihlašovacích údajů a mohlo zavádět bezpečnostní slabiny, pokud byly přihlašovací údaje na aplikační úrovni slabé nebo špatně spravované.

AKMA a konkrétně KAF byly vytvořeny, aby využily silnou primární autentizaci provedenou jádrem sítě 3GPP (5GC) pro zabezpečení přístupu k aplikacím. Jejich účelem je umožnit bezproblémové a bezpečné inicializování aplikační bezpečnosti. Odvozením KAF z již navázané síťové autentizace odstraňuje potřebu, aby uživatel prováděl samostatné přihlášení pro důvěryhodné aplikace. To je zvláště cenné pro služby, které vyžadují ověřenou identitu mobilního účastníka, a pro scénáře IoT, kde je manuální zásah nemožný.

Motivace vychází z potřeby standardizovaného, na síti založeného autentizačního rámce pro aplikace, který přesahuje základní zabezpečení přístupu k síti. Řeší omezení předchozích přístupů, kdy byla bezpečnost aplikací izolována. KAF poskytuje standardizovaný způsob, jak mohou aplikační funkce (AF) získat kryptograficky silné klíče vázané na prokázanou identitu účastníka, což umožňuje nové obchodní modely, jako je identita jako služba, a zabezpečené zpřístupnění služeb IoT přímo z kotvového bodu důvěry sítě 3GPP.

## Klíčové vlastnosti

- Odvozen z kořenového AKMA Anchor Key (KAKMA), což zajišťuje kryptograficky silný řetězec důvěry.
- Jednoznačně vázán na konkrétní UE a konkrétní identitu aplikační funkce (AF) pro oddělení klíčů.
- Umožňuje relace TLS-PSK a dalších zabezpečených aplikačních protokolů bez autentizace vyžadující zásah uživatele.
- Distribuované generování: vypočítán nezávisle UE a AAnF na základě sdílených parametrů.
- Životní cyklus spravován sítí, typicky sladěn s registračním stavem UE.
- Umožňuje AF ověřit identitu a stav účastníka na základě síťové autentizace.

## Související pojmy

- [AKMA – Authentication and Key Management for Applications](/mobilnisite/slovnik/akma/)
- [KAKMA – AKMA Anchor Key](/mobilnisite/slovnik/kakma/)

## Definující specifikace

- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps

---

📖 **Anglický originál a plná specifikace:** [KAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/kaf/)
