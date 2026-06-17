---
slug: "epuid"
url: "/mobilnisite/slovnik/epuid/"
type: "slovnik"
title: "EPUID – EPC ProSe User ID"
date: 2025-01-01
abbr: "EPUID"
fullName: "EPC ProSe User ID"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/epuid/"
summary: "Jedinečný identifikátor přiřazený uživateli pro služby komunikace na krátkou vzdálenost (ProSe) v Evolved Packet Core (EPC). Používá se k vyhledání a přímé komunikaci s blízkými zařízeními podporující"
---

EPUID je jedinečný identifikátor přiřazený uživateli pro služby komunikace na krátkou vzdálenost (ProSe) v Evolved Packet Core, který umožňuje přímé zjišťování a komunikaci mezi zařízeními bez směrování přes síťové jádro.

## Popis

EPC ProSe User ID (EPUID) je klíčový identifikátor v architektuře 3GPP pro služby komunikace na krátkou vzdálenost (ProSe), definovaný napříč specifikacemi jako TS 23.303, TS 29.343 a TS 29.345. Jednoznačně identifikuje uživatele (přesněji účastníka s podporou ProSe) v kontextu funkcí ProSe v EPC. EPUID používají síťové entity ProSe – primárně funkce ProSe – ke správě účastnických dat souvisejících s ProSe, autorizaci schopností ProSe a usnadnění přímého zjišťování a komunikace mezi blízkými UE. Liší se od jiných účastnických identifikátorů, jako je [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/), protože je specifický pro služební vrstvu ProSe.

Architektonicky je EPUID uložen a spravován uvnitř funkce ProSe v domovské síti účastníka. Když se UE zaregistruje pro služby ProSe, funkce ProSe pro tohoto uživatele přidělí nebo namapuje EPUID. Tento identifikátor se pak používá v signalizaci mezi síťovými funkcemi, například mezi funkcí ProSe a aplikačním serverem ProSe nebo mezi funkcemi ProSe v různých sítích (pro scénáře roamingu). Pro přímé zjišťování může UE vysílat kód aplikace ProSe odvozený od jejího ID aplikace ProSe, který může být sítí (pomocí funkce ProSe) převeden na odpovídající EPUID, aby bylo možné zjišťování bez odhalení trvalých identifikátorů přes rozhraní.

EPUID hraje ústřední roli v zabezpečení a ochraně soukromí u ProSe. Umožňuje síti autorizovat a sledovat aktivity ProSe bez nutnosti vystavit trvalou identitu uživatele (IMSI) jiným UE nebo dokonce aplikační vrstvě. Funkce ProSe používá EPUID k získání profilu předplatného ProSe účastníka z [HSS](/mobilnisite/slovnik/hss/) a k vynucování politik. V přímé komunikaci (ProSe Direct Communication) lze EPUID použít uvnitř sítě k navázání bezpečnostních kontextů a správě skupin pro komunikaci jeden-na-jeden nebo jeden-na-mnoho. Jeho formát a struktura jsou definovány tak, aby zajistily globální jedinečnost v rámci domény ProSe a často jsou konstruovány na základě předplatitelských dat uživatele.

## K čemu slouží

EPUID byl zaveden ve 3GPP Release 12 jako součást standardizace služeb komunikace na krátkou vzdálenost (ProSe), které umožňují zjišťování a komunikaci mezi zařízeními. Jeho vytvoření bylo motivováno potřebou vyhrazeného identifikátoru na služební vrstvě, který by mohl podporovat nové případy použití, jako jsou komunikace pro veřejnou bezpečnost, zjišťování pro sociální sítě a komerční služby [D2D](/mobilnisite/slovnik/d2d/), aniž by byla ohrožena ochrana soukromí uživatelů nebo přetíženy stávající identifikátory síťového jádra.

Vyřešil problém, jak jedinečně a bezpečně identifikovat uživatele v rámci služebního rámce ProSe. Použití trvalých identifikátorů, jako je [IMSI](/mobilnisite/slovnik/imsi/), pro zjišťování přes rozhraní by představovalo významná rizika pro ochranu soukromí. EPUID poskytuje vrstvu abstrakce, která umožňuje síti mapovat dočasné kódy nebo identifikátory ProSe používané přes rozhraní na stabilní interní síťovou identitu uživatele pro autorizaci a správu. To umožňuje řízené zjišťování, kde síť může ověřit oprávnění před odhalením přítomnosti nebo kontaktních informací uživatele. EPUID je zásadní pro síťově řízenou architekturu ProSe a odlišuje ji od ad-hoc řešení jako Wi-Fi Direct tím, že poskytuje zabezpečení, účtování a interoperabilitu spravovanou operátorem.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro účastníka ProSe v rámci domény EPC
- Spravován a přidělován funkcí ProSe domovské sítě
- Používán pro autorizaci, kontrolu předplatného a správu služeb v ProSe
- Umožňuje ochranu soukromí oddělením kódů pro zjišťování přes rozhraní od trvalých identit uživatele
- Nezbytný pro síťově řízené zjišťování ProSe a navázání přímé komunikace
- Odkazován v signalizaci mezi funkcemi ProSe, HSS a aplikačními servery ProSe

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.303** (Rel-19) — Proximity Services (ProSe) Stage 2
- **TS 29.343** (Rel-19) — PC2 Reference Point Stage 3 Specification
- **TS 29.345** (Rel-19) — Diameter-based PC6/PC7 interfaces for ProSe
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS

---

📖 **Anglický originál a plná specifikace:** [EPUID na 3GPP Explorer](https://3gpp-explorer.com/glossary/epuid/)
