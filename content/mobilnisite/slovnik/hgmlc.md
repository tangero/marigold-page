---
slug: "hgmlc"
url: "/mobilnisite/slovnik/hgmlc/"
type: "slovnik"
title: "HGMLC – Home Gateway Mobile Location Centre"
date: 2025-01-01
abbr: "HGMLC"
fullName: "Home Gateway Mobile Location Centre"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hgmlc/"
summary: "Home Gateway Mobile Location Centre (HGMLC) je základní síťový uzel zodpovědný za lokalizační služby v domovské síti účastníka. Slouží jako primární rozhraní pro externí aplikace založené na poloze, z"
---

HGMLC je základní síťový uzel v domovské síti účastníka, který poskytuje lokalizační služby a funguje jako primární rozhraní pro externí aplikace tím, že zajišťuje autorizaci, ochranu soukromí a směrování lokalizačních požadavků.

## Popis

Home Gateway Mobile Location Centre (HGMLC) je centrální komponenta architektury lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) dle 3GPP, definovaná jako součást řídicí roviny. Nachází se v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) účastníka. HGMLC slouží jako primární vstupní bod pro externí klienty lokalizačních služeb (LCS klienty) žádající o polohu uživatelského zařízení (UE). Jeho základní rolí je autorizovat a ověřovat tyto externí požadavky na základě identity klienta a nastavení ochrany soukromí účastníka, čímž zajišťuje soulad s regulatorními požadavky, jako jsou například požadavky pro tísňové služby (např. E911) a zákonný odposlech.

Z architektonického hlediska HGMLC komunikuje s několika síťovými entitami. S Visited Gateway Mobile Location Centre (VGMLC) v navštívené síti komunikuje, když je cílové UE v roamingu, a to pomocí rozhraní Lh. Pro účastníky ve své domovské síti komunikuje s Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/))/Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) prostřednictvím rozhraní Lg. HGMLC také komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) za účelem získání dat o účastníkovi a směrovacích informací. Základním protokolem pro tuto komunikaci je Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) pro sítě s přepojováním okruhů nebo Diameter pro sítě s přepojováním paketů, jak je specifikováno v 3GPP TS 29.503.

Fungování HGMLC zahrnuje několik klíčových kroků. Po přijetí lokalizačního požadavku od LCS klienta ověří autorizaci klienta pro službu. Poté zkontroluje profil ochrany soukromí cílového účastníka, který definuje, komu je umožněno lokalizovat UE a za jakých podmínek. Pokud je požadavek autorizován, HGMLC určí aktuální obsluhující uzel UE (např. MSC, SGSN, MME, AMF). Pokud se UE nachází v jeho domovské síti, HGMLC přepošle lokalizační požadavek příslušnému uzlu. Pokud je UE v roamingu, směruje požadavek na VGMLC v navštívené síti. HGMLC následně obdrží od sítě odhad polohy (např. zeměpisné souřadnice) a předá jej žádajícímu LCS klientovi.

Jeho role přesahuje pouhé směrování požadavků. HGMLC je zodpovědný za korelaci účtování pro lokalizační transakce, vede záznamy pro audit a podporuje odložené lokalizační požadavky (např. periodické nebo spouštěné hlášení polohy). V kontextu 5G jsou funkce HGMLC integrovány do architektury Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) a Network Exposure Function (NEF), ale logické oddělení odpovědností mezi domovskou a navštívenou sítí zůstává klíčovým konceptem pro scénáře mezi operátory a roaming.

## K čemu slouží

HGMLC byl zaveden za účelem poskytnutí standardizované, bezpečné a škálovatelné architektury pro poskytování lokalizačních služeb v mobilních sítích. Před jeho standardizací byly lokalizační služby často proprietární, což omezovalo interoperabilitu mezi dodavateli síťového vybavení a mezi sítěmi různých operátorů. HGMLC řeší potřebu centralizované entity řízené domovskou sítí pro správu externího přístupu k lokalizačním datům účastníka, což je vysoce citlivý zdroj.

Primární problémy, které řeší, jsou ochrana soukromí, zabezpečení a koordinace mezi operátory. Vynucuje zásady ochrany soukromí účastníka a brání neoprávněnému sledování. Poskytuje jednotnou, zabezpečenou bránu pro lokalizační klienty třetích stran, čímž zjednodušuje síťové bezpečnostní politiky. Pro účastníky v roamingu umožňuje domovské síti zachovat kontrolu nad autorizací a účtováním lokalizačních služeb, zatímco samotné určení polohy deleguje na infrastrukturu navštívené sítě prostřednictvím VGMLC. Tento model je klíčový pro globální roamingové dohody.

Jeho vytvoření bylo motivováno rostoucí poptávkou po komerčních službách založených na poloze (např. navigace, vyhledávače přátel) a přísnými regulatorními požadavky na lokalizaci tísňových volajících (E-911 v USA, E-112 v Evropě). Architektura HGMLC umožňuje operátorům nabízet tyto služby kontrolovaným a zúčtovatelným způsobem, přičemž chrání práva účastníků a plní zákonné povinnosti týkající se poskytování tísňových služeb.

## Klíčové vlastnosti

- Slouží jako primární brána pro externí klienty lokalizačních služeb (LCS klienty) v domovské síti
- Vynucuje ověření ochrany soukromí účastníka a autorizaci LCS klienta
- Směruje lokalizační požadavky na příslušný síťový uzel (MSC, SGSN, MME, VGMLC)
- Podporuje lokalizační služby mezi PLMN prostřednictvím rozhraní s Visited GMLC (VGMLC)
- Zajišťuje korelaci účtování a logování transakcí lokalizačních služeb
- Umožňuje okamžité i odložené (periodické/spouštěné) hlášení polohy

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3

---

📖 **Anglický originál a plná specifikace:** [HGMLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/hgmlc/)
