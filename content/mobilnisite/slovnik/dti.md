---
slug: "dti"
url: "/mobilnisite/slovnik/dti/"
type: "slovnik"
title: "DTI – Direct Tunnel Indication"
date: 2025-01-01
abbr: "DTI"
fullName: "Direct Tunnel Indication"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dti/"
summary: "Direct Tunnel Indication (DTI) je parametr používaný v protokolu GTP-C k signalizaci podpory a žádosti o zřízení přímého tunelu uživatelské roviny mezi Serving Gateway (SGW) a Packet Data Network Gate"
---

DTI je parametr protokolu GTP-C používaný k signalizaci podpory a žádosti o zřízení přímého tunelu uživatelské roviny mezi SGW a PGW, který obejde SGW za účelem optimalizace datové cesty v EPC.

## Popis

Direct Tunnel Indication (DTI) je příznak nebo informační prvek v rámci [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol pro řídicí rovinu ([GTP-C](/mobilnisite/slovnik/gtp-c/)), specifikovaný v 3GPP TS 29.060 a TS 23.060. Používá se během procedur aktivace nebo modifikace přenosového kanálu, například ve zprávách Create Session Request, Modify Bearer Request nebo Create PDP Context Request. Primární funkcí DTI je indikovat, zda vysílací uzel (typicky [MME](/mobilnisite/slovnik/mme/) v EPS nebo SGSN v GPRS/UMTS) podporuje a/nebo si přeje zřízení „přímého tunelu“ pro uživatelskou rovinu. Přímý tunel označuje [GTP-U](/mobilnisite/slovnik/gtp-u/) tunel pro uživatelská data, který je zřízen přímo mezi Serving Gateway (SGW) a Packet Data Network Gateway (PGW) v EPC, nebo mezi GGSN a RNC v kontextu UMTS, čímž se efektivně umožní obejít přeposílací funkci SGW pro určitý provoz.

Jak to funguje, zahrnuje vyjednávání během signalizace správy relace. Když MME podporující funkci přímého tunelu iniciuje Create Session Request směrem k SGW, může zahrnout DTI nastavené na hodnotu indikující „Přímý tunel možný“. SGW po přijetí této informace chápe, že může být instruováno k zřízení GTP-U tunelu přímo s PGW, namísto toho, aby tok uživatelských dat vedl z PGW přes SGW k eNodeB. Pokud jsou splněny všechny podmínky (např. SGW a PGW to také podporují a neexistují specifické požadavky na zákonné odposlechy nebo účtování, které by vyžadovaly kotvení v SGW), SGW přistoupí k vytvoření přímého tunelu. SGW pak zahrne své vlastní DTI ve zprávě k PGW. Výsledná architektura snižuje latenci a odstraňuje zbytečnou procesní zátěž na SGW pro datovou cestu.

Její role v síti je optimalizační. Při standardním provozu bez přímého tunelu procházejí všechny pakety uživatelské roviny SGW, které provádí úkoly jako zákonný odposlech, sběr účtovacích dat a vyrovnávací paměť downlink paketů. Použitím DTI k povolení přímého tunelu je datová cesta zefektivněna, což je zvláště výhodné pro služby s vysokou propustností a nízkou latencí. SGW zůstává v řídicí cestě, spravuje kontexty přenosových kanálů a zpracovává události mobility, ale je odstraněno z roviny přeposílání uživatelských dat v reálném čase pro indikovaný přenosový kanál, což vede k distribuovanější a efektivnější architektuře EPC.

## K čemu slouží

DTI bylo zavedeno, aby řešilo potřebu efektivnější a nižší latence architektury uživatelské roviny v rámci 3GPP paketového jádra, zejména s evolucí směrem k Evolved Packet System (EPS) v Release 8 a optimalizací dřívějších systémů [GPRS](/mobilnisite/slovnik/gprs/). Problém, který řeší, je suboptimální „tromboning“ nebo „hairpinning“ uživatelských dat přes SGW ve všech scénářích. V základní architektuře by každý paket mezi UE a internetem putoval po trase PGW<->SGW<->eNodeB, i když je UE stacionární a funkce SGW, jako je kotvení mobility, nejsou aktivně vyžadovány. To přidává zbytečnou latenci a zátěž.

Motivace pro její vytvoření, zejména zaznamenaná od jejího zavedení v Rel-7 pro UMTS a vylepšení v EPS, byla optimalizovat datovou cestu pro specifické typy provozu nebo stavy, například když je UE ve stabilním aktivním stavu bez bezprostředních potřeb mobility. Umožnila operátorům navrhovat sítě, kde může být SGW pro určité vysoce výkonné datové relace obejito, čímž se sníží jak kapitálové výdaje (snížením požadavků na zpracování SGW), tak provozní výdaje (nižšími náklady na přenos a zlepšenou kvalitou služeb). DTI poskytlo standardizovaný, vyjednaný mechanismus k umožnění této optimalizace, což přesahuje proprietární řešení a zajišťuje interoperabilitu více dodavatelů pro nasazení přímých tunelů.

## Klíčové vlastnosti

- Informační prvek GTP-C používaný k signalizaci podpory a žádosti o přímou cestu uživatelské roviny.
- Umožňuje zřízení přímého GTP-U tunelu mezi SGW a PGW (nebo mezi GGSN a RNC v UMTS).
- Vyjednává se během procedur správy relace, jako je Create Session nebo Aktivace PDP kontextu.
- Optimalizuje uživatelskou rovinu tím, že obejde SGW pro přeposílání dat, čímž snižuje latenci a zátěž.
- Zachovává SGW v řídicí rovině pro správu přenosových kanálů a mobility.
- Specifikováno v základních protokolech 3GPP (GTP-C), což zajišťuje standardizovanou implementaci napříč síťovými elementy.

## Související pojmy

- [GTP-C – GPRS Tunnelling Protocol for Control Plane](/mobilnisite/slovnik/gtp-c/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 32.406** (Rel-19) — Performance Management for CN PS Domain
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes

---

📖 **Anglický originál a plná specifikace:** [DTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/dti/)
