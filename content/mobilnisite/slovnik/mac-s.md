---
slug: "mac-s"
url: "/mobilnisite/slovnik/mac-s/"
type: "slovnik"
title: "MAC-S – Resynchronisation Authentication Code"
date: 2025-01-01
abbr: "MAC-S"
fullName: "Resynchronisation Authentication Code"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mac-s/"
summary: "Kryptografický kód používaný v UMTS a LTE pro bezpečnou resynchronizaci autentizačních vektorů mezi UE a sítí po selhání. Zabrání opakovaným útokům (replay attacks) a zajišťuje integritu procesu resyn"
---

MAC-S je kryptografický kód používaný v UMTS a LTE pro bezpečnou resynchronizaci autentizačních vektorů mezi UE a sítí po selhání, který zabraňuje opakovaným útokům (replay attacks) a zajišťuje integritu procedury.

## Popis

Resynchronisation Authentication Code (MAC-S) je klíčový bezpečnostní mechanismus definovaný v rámci protokolu Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) pro systémy 3GPP, především UMTS a později rozšířený pro LTE a 5G. Funguje jako Message Authentication Code ([MAC](/mobilnisite/slovnik/mac/)) specificky generovaný k ochraně procedury resynchronizace. Tato procedura se spustí, když se pořadové číslo (SQN) používané v protokolu AKA rozchází mezi uživatelským zařízením (UE) a autentizačním centrem sítě (AuC), což je stav známý jako 'synchronizační selhání'. MAC-S je vypočteno AuC pomocí kryptografického algoritmu (např. MILENAGE) se vstupy zahrnujícími tajný klíč účastníka (K), náhodnou výzvu (RAND), nové pořadové číslo (SQN<sub>new</sub>) a další parametry. Tento vypočtený MAC-S je následně odeslán do UE uvnitř tokenu [AUTS](/mobilnisite/slovnik/auts/), který je součástí zprávy Synchronisation Failure.

Po přijetí tokenu AUTS si UE nezávisle vypočte vlastní očekávanou hodnotu MAC-S pomocí stejných vstupů (K, RAND, SQN<sub>new</sub>) a stejného algoritmu. UE pak porovná přijatý MAC-S s lokálně vypočtenou hodnotou. Pokud se shodují, může UE kryptograficky ověřit, že žádost o resynchronizaci pochází od legitimní síťové entity, která zná sdílený tajný klíč K, a že nové pořadové číslo SQN<sub>new</sub> nebylo během přenosu pozměněno. Toto ověření je klíčové; zabraňuje útočníkovi vynutit vrácení pořadového čísla nebo vložit škodlivý příkaz k resynchronizaci, což by jinak mohlo vést k opakovaným útokům nebo odmítnutí služby.

Architektura pro MAC-S zahrnuje UE, obsluhující síť (např. VLR/SGSN, [MME](/mobilnisite/slovnik/mme/)) a AuC domovské sítě. AuC je jedinou entitou, která generuje platný MAC-S, protože je to jediný síťový uzel kromě UE, který vlastní dlouhodobý tajný klíč K. Obsluhující síť funguje jako přenosový článek, který předává token AUTS z UE do domovské sítě a následný autentizační vektor s novým SQN zpět do UE. Role MAC-S je jedinečná, ale kritická: poskytuje integritu a autentizaci původu dat specificky pro hodnotu resynchronizace SQN, čímž zajišťuje, že základní protokol AKA se může ze desynchronizace bezpečně zotavit, aniž by byla ohrožena celková autentizační struktura. Jeho správná implementace je povinnou součástí souladu se specifikacemi zabezpečení 3GPP.

## K čemu slouží

MAC-S byl zaveden, aby řešil specifickou zranitelnost ve správě stavu protokolu [AKA](/mobilnisite/slovnik/aka/). Protokol AKA používá pořadové číslo (SQN) k zajištění čerstvosti a zabránění opakovanému použití autentizačních vektorů. Nicméně síťová selhání, zpoždění nebo škodlivé zásahy mohou způsobit, že se SQN udržované UE a AuC rozcházejí. Bez bezpečného mechanismu obnovy by tato desynchronizace vedla k trvalým autentizačním selháním, což by legitimnímu uživateli efektivně odepřelo službu. Rané mechanismy pro resynchronizaci pořadových čísel byly potenciálně nezabezpečené a riskovaly manipulaci ze strany útočníka.

Vytvoření MAC-S poskytlo kryptograficky zabezpečené řešení tohoto problému. Umožňuje síti navrhnout UE nové, synchronizované pořadové číslo se zárukou autenticity. Tím se řeší problém s odmítnutím služby a zároveň se aktivně předchází bezpečnostním hrozbám. Útočník nemůže zfalšovat platný MAC-S bez znalosti tajného klíče K a nemůže znovu použít starý MAC-S, protože je vázán na konkrétní RAND a SQN<sub>new</sub>. MAC-S tedy umožňuje robustní obnovu ze synchronizačních selhání, což je nezbytná vlastnost pro jakýkoli rozsáhlý a spolehlivý celulární systém, kde jsou taková selhání statisticky nevyhnutelná kvůli obrovskému počtu zařízení a transakcí.

## Klíčové vlastnosti

- Poskytuje ochranu integrity a autentizaci původu dat pro nové pořadové číslo (SQN<sub>new</sub>) během resynchronizace.
- Generován pomocí kryptografického algoritmu (např. MILENAGE) a sdíleného tajného klíče K.
- Přenášen uvnitř tokenu AUTS z UE do sítě pro nahlášení synchronizačního selhání.
- Umožňuje UE ověřit síťový příkaz k resynchronizaci, čímž zabraňuje škodlivé manipulaci s SQN.
- Nezbytný pro obnovu z neshod pořadových čísel v protokolu AKA bez přerušení služby.
- Klíčová komponenta procedury Synchronisation Failure v AKA pro UMTS/LTE/5G.

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [AUTS – Re-synchronisation Token](/mobilnisite/slovnik/auts/)

## Definující specifikace

- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [MAC-S na 3GPP Explorer](https://3gpp-explorer.com/glossary/mac-s/)
