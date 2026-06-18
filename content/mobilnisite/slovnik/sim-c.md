---
slug: "sim-c"
url: "/mobilnisite/slovnik/sim-c/"
type: "slovnik"
title: "SIM-C – SEAL Identity Management Client"
date: 2025-01-01
abbr: "SIM-C"
fullName: "SEAL Identity Management Client"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sim-c/"
summary: "Funkční komponenta uvnitř zařízení, která vystupuje jako klient v rámci architektury pro správu identit SEAL. Komunikuje se serverem SIM-S za účelem zřizování, správy a ověřování identit pro zabezpeče"
---

SIM-C je klientská komponenta v rámci architektury pro správu identit SEAL, která komunikuje se serverem SIM-S za účelem zřizování, správy a ověřování identit pro zabezpečené edge aplikace.

## Popis

[SEAL](/mobilnisite/slovnik/seal/) Identity Management Client (SIM-C) je definovaná funkční entita v rámci architektury 3GPP SEAL (Service Enabler Architecture Layer), konkrétně pro modul pro správu identit (Identity Management Enabler). Nachází se v uživatelském zařízení (UE) nebo v klientské edge aplikaci. SIM-C je zodpovědný za iniciaci a účast v protokolech pro správu decentralizovaných identit a ověřitelných přihlašovacích údajů (verifiable credentials) podle specifikace architektury SEAL. Spolupracuje se serverem pro správu identit SEAL ([SIM-S](/mobilnisite/slovnik/sim-s/)) při plnění operací souvisejících s identitou.

Z architektonického hlediska SIM-C implementuje klientskou logiku protokolů pro správu identit SEAL. Mezi jeho klíčové funkce patří generování nebo přijímání decentralizovaných identifikátorů (DID), formulace žádostí o ověřitelné přihlašovací údaje a bezpečné ukládání přijatých přihlašovacích údajů. Komunikuje se SIM-S, který často vystupuje jako zprostředkovatel nebo držitel důvěryhodných kotviv (jako je DID resolver nebo registr ověřitelných dat). Komunikace mezi SIM-C a SIM-S typicky využívá RESTful [API](/mobilnisite/slovnik/api/) přes zabezpečené transportní vrstvy (např. [TLS](/mobilnisite/slovnik/tls/)), jak je definováno v příslušných specifikacích 3GPP. SIM-C také může komunikovat s lokálními zabezpečenými prvky (jako je [USIM](/mobilnisite/slovnik/usim/) nebo hardwarový bezpečnostní modul) za účelem ochrany privátních klíčů spojených s jeho DID.

Jeho fungování zahrnuje několik klíčových procesů. Za prvé, při zřizování identity může SIM-C požádat o vystavení ověřitelného přihlašovacího údaje od vystavovatele, případně prostřednictvím SIM-S. To může zahrnovat předložení důkazů o existujících atributech. Za druhé, pro ověření identity nebo přístup ke službě SEAL může být SIM-C vyzván k předložení ověřitelného přihlašovacího údaje. Načte příslušný přihlašovací údaj ze svého zabezpečeného úložiště, případně vytvoří ověřitelné předložení (presentation) (což může zahrnovat generování kryptografického důkazu) a odešle jej ověřovateli (kterým může být SIM-S nebo jiná komponenta SEAL). SIM-C zajišťuje kryptografické operace potřebné pro vytváření a ověřování těchto předložení, přičemž využívá klíče vázané na jeho DID. Jeho role je klíčová pro umožnění uživateli nebo zařízení prokázat určité atributy (např. stav předplatného, roli, věk) edge aplikacím způsobem, který zachovává soukromí a je decentralizovaný, bez nutnosti vždy přímé interakce s jádrem mobilní sítě pro účely ověřování.

## K čemu slouží

SIM-C byl vytvořen, aby řešil výzvy spojené se správou identit a přístupu, které jsou vlastní distribuovaným edge výpočetním systémům a architekturám pro povolování služeb, jako je [SEAL](/mobilnisite/slovnik/seal/). Tradiční ověřování v mobilních sítích (např. prostřednictvím [USIM](/mobilnisite/slovnik/usim/)/[AKA](/mobilnisite/slovnik/aka/)) je centralizované kolem jádra sítě a primárně slouží pro přístup k síti. Edge aplikace a služby třetích stran však vyžadují flexibilnější mechanismy identity na aplikační vrstvě, které mohou potvrdit specifické atributy uživatele/zařízení, aniž by vždy musely procházet jádrem sítě.

Problém, který řeší, je poskytnutí standardizované, zabezpečené klientské komponenty, která se může účastnit moderních, decentralizovaných paradigmat identity (jako jsou ta založená na standardech W3C Verifiable Credentials a DID) v rámci telekomunikačního ekosystému. Předchozí přístupy se buď spoléhaly na proprietární, neinteroperabilní ověřování na aplikační úrovni, nebo směrovaly všechny kontroly identity zpět do jádra sítě domovského operátora, což je neefektivní pro edge služby s nízkou latencí. SIM-C jako součást architektury SEAL umožňuje zařízením získávat a používat ověřitelné přihlašovací údaje, které mohou být nezávisle ověřeny edge uzly, což umožňuje důvěryhodné interakce v edge prostředích s více doménami a více dodavateli.

Jeho vytvoření bylo motivováno potřebou propojit telekomunikační úroveň zabezpečení s flexibilitou webových modelů identity. Umožňuje poskytovatelům služeb na edge využít důvěru odvozenou z mobilního předplatného (např. přihlašovací údaj vystavený operátorem) a zároveň podporovat funkce zaměřené na uživatele a zlepšující soukromí, jako je selektivní zveřejňování. To usnadňuje nové obchodní modely pro edge služby, zabezpečené připojování IoT zařízení a bezproblémové ověřování napříč službami v sítích 5G a budoucích.

## Klíčové vlastnosti

- Klientská implementace protokolů pro správu identit SEAL pro decentralizovanou identitu
- Správa decentralizovaných identifikátorů (DID) a přidruženého kryptografického klíčového materiálu
- Zabezpečené ukládání a manipulace s ověřitelnými přihlašovacími údaji (Verifiable Credentials) přijatými od vystavovatelů
- Schopnost vytvářet ověřitelná předložení (Verifiable Presentations) pro prokazování tvrzení (claims) stranám spoléhajícím na důkaz/ověřovatelům
- Rozhraní se serverem pro správu identit SEAL (SIM-S) využívající standardizovaná API
- Může využívat základní zabezpečení zařízení (např. vazbu na UICC/USIM) pro ochranu klíčů

## Související pojmy

- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [SIM-S – SEAL Identity Management Server](/mobilnisite/slovnik/sim-s/)

## Definující specifikace

- **TS 24.547** (Rel-19) — SEAL Identity Management Protocol
- **TS 33.434** (Rel-19) — Security aspects of SEAL for verticals

---

📖 **Anglický originál a plná specifikace:** [SIM-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/sim-c/)
