---
slug: "pqfi"
url: "/mobilnisite/slovnik/pqfi/"
type: "slovnik"
title: "PQFI – PC5 QoS Flow Identifier"
date: 2025-01-01
abbr: "PQFI"
fullName: "PC5 QoS Flow Identifier"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pqfi/"
summary: "PC5 QoS Flow Identifier (PQFI) je jedinečný identifikátor přiřazený konkrétnímu toku QoS zřízenému přes referenční bod PC5 pro přímou komunikaci mezi zařízeními. Umožňuje přesné mapování a vynucování"
---

PQFI je jedinečný identifikátor konkrétního toku QoS přes referenční bod PC5, který umožňuje přesné mapování a vynucování QoS pro jednotlivé datové toky v sidelink komunikaci, jako je V2X.

## Popis

PC5 QoS Flow Identifier (PQFI) je základní součástí architektury 3GPP pro správu kvality služeb (QoS) na rozhraní PC5, což je referenční bod pro přímou komunikaci mezi uživatelskými zařízeními (UE) bez průchodu síťovou infrastrukturou (sidelink). Každému zřízenému toku QoS přes rozhraní PC5 je přiřazena jedinečná hodnota PQFI. Tento identifikátor se používá koncově mezi komunikujícími UE k rozlišení a správě paketových toků podle jejich specifických profilů QoS, které jsou definovány parametry jako priorita, rozpočet zpoždění paketu, míra chybovosti paketů a datový tok.

Z architektonického hlediska PQFI funguje uvnitř protokolového zásobníku UE, konkrétně na vrstvě, kde se toky QoS mapují na datové rádiové nosiče nebo sidelink rádiové nosiče pro přenos přes rozhraní vzduchu. Když je pro relaci PC5 komunikace odvozena priorita [ProSe](/mobilnisite/slovnik/prose/) na úrovni paketu ([PPPP](/mobilnisite/slovnik/pppp/)) nebo identifikátor 5G QoS ([5QI](/mobilnisite/slovnik/5qi/)), je odpovídající tok QoS zřízen a označen PQFI. Tento identifikátor je pak zahrnut v hlavičkách paketů nebo asociován s kontextem toku, což umožňuje vysílajícím i přijímajícím UE, stejně jako případným přenosovým (relay) UE, aplikovat správné zpracování QoS, včetně plánování, řízení přístupu a přidělování prostředků.

Role PQFI je klíčová ve scénářích vyžadujících více souběžných služeb s různými požadavky přes jeden spoj PC5. Například vozidlo může současně provozovat bezpečnostně kritickou aplikaci pro zabránění kolizi (vyžadující ultra-nízkou latenci a vysokou spolehlivost) a infotainmentovou službu (vyžadující vysokou přenosovou kapacitu). PQFI umožňuje UE klasifikovat pakety z těchto různých aplikací do samostatných toků QoS, každý se svým vlastním identifikátorem, a zajistit tak, že přísné požadavky bezpečnostní aplikace nejsou narušeny přenosově náročným infotainmentovým provozem. Správa hodnot PQFI, včetně jejich přiřazení, změny a uvolnění, se řídí postupy definovanými ve specifikacích 3GPP, často spouštěnými požadavky na zřízení nebo změnu relace.

V širším rámci QoS PQFI spolupracuje s dalšími identifikátory, jako je PC5 QoS Identifier ([PQI](/mobilnisite/slovnik/pqi/)), který definuje šablonu charakteristik QoS, a PC5 Link Identifier. PQFI poskytuje podrobnost potřebnou pro vynucování QoS na úrovni jednotlivých toků, zatímco PQI poskytuje standardizovaný profil. Toto oddělení umožňuje flexibilní a efektivní správu QoS, včetně dynamické adaptace na měnící se požadavky služeb a rádiové podmínky bez nutnosti předefinovávat celý profil QoS pro každý paket.

## K čemu slouží

PQFI byl zaveden, aby řešil potřebu sofistikované správy QoS v přímé komunikaci mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)), zejména pro služby komunikace vozidla se vším ([V2X](/mobilnisite/slovnik/v2x/)) a služeb veřejné bezpečnosti standardizované od 3GPP Release 16 a novějších. Před jeho zavedením měla sidelink komunikace v dřívějších releasech omezenější QoS mechanismy, které se často spoléhaly na široké třídy služeb nebo priority (jako [PPPP](/mobilnisite/slovnik/pppp/)) bez detailního rozlišení na úrovni toků potřebného pro pokročilé případy užití. Vývoj směrem k autonomnímu řízení a pokročilým V2X aplikacím vytvořil poptávku po podpoře více souběžných datových proudů s různorodými a přísnými požadavky přes jediný spoj PC5.

Primární problém, který PQFI řeší, je neschopnost jednoznačně identifikovat a spravovat jednotlivé toky QoS v rámci relace PC5 komunikace. Bez takového identifikátoru by se veškerý provoz mezi dvěma UE zpracovával homogenně, což by znemožňovalo garantovat výkon pro kritické služby na pozadí běžného provozu. PQFI umožňuje síti a UE aplikovat specifické QoS politiky na úrovni jednotlivých toků, čímž zajišťuje, že latenci citlivé bezpečnostní zprávy mají přednost před nekritickými daty. Tato detailní kontrola je nezbytná pro dosažení výkonnostních cílů stanovených pro pokročilé V2X služby, které jsou základem bezpečnosti silničního provozu a efektivity dopravy.

Jeho vytvoření bylo motivováno širším úsilím 3GPP o integraci sidelink komunikace do systému 5G s rámcem QoS srovnatelné schopnosti jako rozhraní Uu (UE-síť). Umožňuje rozšířit principy 5G QoS, jako je přeposílání na základě toků a detailní správa prostředků, na přímé spoje mezi UE. Tím zajišťuje konzistentní a výkonný uživatelský zážitek napříč všemi režimy komunikace, ať už provoz prochází sítí, nebo přímo mezi zařízeními, a naplňuje tak vizi 5G o podpoře ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) v D2D scénářích.

## Klíčové vlastnosti

- Jednoznačně identifikuje konkrétní tok QoS v rámci relace PC5 komunikace
- Umožňuje vynucování QoS politik na úrovni jednotlivých toků pro sidelink přenosy
- Spolupracuje s PQI pro mapování toků na standardizované charakteristiky QoS
- Podporuje souběžné více služeb s různými požadavky na jediném spoji PC5
- Usnadňuje plánování paketů a přidělování rádiových prostředků s ohledem na QoS pro sidelink
- Integruje se s rámcem 5G QoS pro konzistentní správu napříč rozhraními Uu a PC5

## Související pojmy

- [PQI – PC5 QoS Identifier](/mobilnisite/slovnik/pqi/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TS 37.324** (Rel-19) — Service Data Adaptation Protocol (SDAP)

---

📖 **Anglický originál a plná specifikace:** [PQFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pqfi/)
