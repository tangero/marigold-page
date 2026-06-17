---
slug: "bra"
url: "/mobilnisite/slovnik/bra/"
type: "slovnik"
title: "BRA – Binding Revocation Acknowledgement"
date: 2025-01-01
abbr: "BRA"
fullName: "Binding Revocation Acknowledgement"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bra/"
summary: "BRA je zpráva protokolu založeného na Diameter používaná v Evolved Packet Core (EPC) 3GPP k potvrzení úspěšného odvolání mobilního vazebního záznamu. Je klíčovou součástí rozhraní Gx, která zajišťuje"
---

BRA je zpráva protokolu Diameter potvrzující úspěšné odvolání mobilního vazebního záznamu (binding revocation) na rozhraní Gx v 3GPP, která zajišťuje ukončení pravidel PCC při skončení IP-CAN relace, čímž předchází problémům s prostředky a účtováním.

## Popis

Binding Revocation Acknowledgement (BRA) je odpověď (Diameter Answer message), konkrétně příkaz Diameter Answer, definovaný v rámci aplikace Gx v 3GPP (specifikováno v 3GPP TS 29.212). Funguje na rozhraní Gx, které spojuje funkci pravidel řízení politiky a účtování (PCRF) a funkci vynucování politiky a účtování (PCEF), typicky umístěnou v Packet Data Network Gateway (PGW) v EPC. BRA je přímá odpověď na příkaz Binding Revocation Request (BRR). Když je [IP-CAN](/mobilnisite/slovnik/ip-can/) relace uživatele ukončena (např. z důvodu odpojení uživatele, selhání sítě nebo administrativní akce), musí PCEF informovat PCRF, aby mohla být odstraněna všechna přidružená pravidla politiky a účtování. PCEF odešle BRR k PCRF. Po úspěšném zpracování této žádosti a odstranění všech pravidel PCC a kontextu relace pro danou IP-CAN relaci odešle PCRF zpět k PCEF BRA, aby potvrdil provedení operace.

Struktura zprávy BRA následuje základní protokol Diameter (RFC 6733) a zahrnuje standardní hlavičku Diameter s Command-Code nastaveným na hodnotu přiřazenou pro BRA. Musí obsahovat atribut Session-Id Attribute-Value Pair ([AVP](/mobilnisite/slovnik/avp/)), který jednoznačně identifikuje rušenou IP-CAN relaci, což zajišťuje správné přiřazení potvrzení k odpovídající žádosti. AVP Result-Code je povinný a udává výsledek žádosti o odvolání; hodnota DIAMETER_SUCCESS (2001) potvrzuje úspěšné odvolání, zatímco jiné kódy chyb indikují selhání, která mohou vyžadovat opakovaný přenos nebo alternativní zpracování. BRA může také obsahovat volitelné AVP pro rozšíření specifická pro výrobce nebo dodatečné diagnostické informace.

Z pohledu provozu sítě BRA dokončuje kritickou signalizační transakci pro správu relací. Její spolehlivé doručení, zajištěné podpůrnými mechanismy pro převzetí služeb při selhání a přenos v základním protokolu Diameter, garantuje synchronizaci stavu politiky v PCRF se stavem přenosu v PCEF. Tím se zabrání scénářům, kdy PCEF považuje relaci za uzavřenou, ale PCRF nadále drží prostředky a kontexty účtování, což by mohlo vést k nesprávnému účtování, konfliktům pravidel politiky pro znovu použité IP adresy a neefektivnímu využití síťových a paměťových prostředků v obou síťových funkcích. BRA je proto základním prvkem pro udržení integrity architektury PCC.

## K čemu slouží

BRA byla zavedena, aby poskytla formální a spolehlivý mechanismus potvrzení pro proceduru odvolání vazebního záznamu v rámci architektury řízení politiky a účtování (PCC) 3GPP. Před její standardizací byla signalizace ukončení relace mezi bránou vynucující politiky (PCEF) a entitou je spravující (PCRF) méně explicitní nebo spoléhala na implicitní časové limity relací, což mohlo vést k desynchronizaci stavu. Tato desynchronizace představovala významné provozní problémy, včetně úniků prostředků v PCRF, nepřesných záznamů o účtování a potenciálních konfliktů politik při přidělení IP adres novým relacím.

Vytvoření BRA společně s BRR tyto nedostatky odstranilo zavedením čistého transakčního dialogu pro ukončení relace. Bylo motivováno potřebou robustního, stavového řízení politiky v plně IP Evolved Packet System (EPS) definovaném od 3GPP Release 8 dále. Jak sítě přecházely na podporu složitějších služeb v reálném čase s jemně odstupňovanými pravidly QoS a účtování, rostly náklady na nesprávný stav politiky. BRA zajišťuje, že PCRF může definitivně potvrdit uvolnění všech pravidel spojených s relací, čímž poskytuje jasnou auditní stopu a umožňuje přesné účtování prostředků. To je nezbytné jak pro efektivitu sítě, tak pro přesnost komerčního účtování v moderních službách mobilního širokopásmového přístupu.

## Klíčové vlastnosti

- Definován jako příkaz Diameter Answer (odpověď) na rozhraní Gx
- Povinná odpověď na příkaz Binding Revocation Request (BRR)
- Nese AVP Result-Code pro indikaci úspěchu nebo selhání odvolání
- Obsahuje AVP Session-Id pro jednoznačnou identifikaci ukončené IP-CAN relace
- Zajišťuje synchronizaci stavu politiky mezi PCRF a PCEF
- Zabraňuje únikům prostředků a nepřesnostem v účtování potvrzením odstranění kontextu

## Definující specifikace

- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [BRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/bra/)
