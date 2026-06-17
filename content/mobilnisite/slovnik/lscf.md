---
slug: "lscf"
url: "/mobilnisite/slovnik/lscf/"
type: "slovnik"
title: "LSCF – Location System Control Function"
date: 2025-01-01
abbr: "LSCF"
fullName: "Location System Control Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lscf/"
summary: "Location System Control Function (LSCF) je centrální řídicí entita v architektuře lokalizačních služeb (LCS) 3GPP. Koordinuje celý proces určení polohy mobilního zařízení, od přijetí lokalizační žádos"
---

LSCF je centrální řídicí entita v architektuře lokalizačních služeb 3GPP, která koordinuje celý proces určování polohy mobilního zařízení od žádosti po doručení výsledku.

## Popis

Location System Control Function (LSCF) je klíčová logická komponenta v standardizované architektuře lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) 3GPP. Slouží jako hlavní řadič a koordinátor všech aktivit souvisejících s určováním polohy ve veřejné pozemní mobilní síti (PLMN). LSCF přijímá lokalizační žádosti z různých zdrojů, ověřuje a autorizuje tyto žádosti, spravuje lokalizační relaci s příslušnými síťovými elementy a nakonec vrací odhadnutou polohu nebo indikaci selhání. Její funkce je klíčová jak pro regulatorní služby, jako je tísňové volání, tak pro komerční nadstavbové služby.

Architektonicky stojí LSCF v srdci systému LCS. V dřívějších vydáních 3GPP byla tato funkce často realizována jako součást Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)). LSCF komunikuje s několika klíčovými entitami: 1) LCS klientem (externí aplikací nebo síťovou entitou žádající o polohu), 2) Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) pro autorizaci účastníka a směrovací informace, 3) Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v jádru sítě pro dosažení cílového uživatelského zařízení (UE), a 4) Serving Mobile Location Centre (SMLC) nebo Evolved Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v rádiové přístupové síti, který provádí vlastní výpočty polohy pomocí měření z UE a/nebo základnových stanic.

Provoz LSCF následuje definovanou sekvenci. Po přijetí lokalizační žádosti nejprve provede validaci, zkontroluje identitu klienta a nastavení soukromí účastníka (LCS profil soukromí), aby zajistil, že je žádost povolena. Poté se dotáže HSS/HLR, aby určil aktuální obsluhující uzel (MSC/MME) pro UE. LSCF přepošle žádost tomuto obsluhujícímu uzlu, který následně zapojí příslušný lokalizační uzel (SMLC/E-SMLC) v RAN. LSCF spravuje tento dialog, případně překládá mezi různými protokolovými zásobníky (např. z externího protokolu [MLP](/mobilnisite/slovnik/mlp/) na interní protokoly RANAP nebo LPP/LPPa). Přijímá měření polohy nebo konečný odhad polohy od SMLC, může provést dodatečné zpracování (jako transformaci souřadnic) a poté výsledek naformátuje a vrátí žádajícímu klientovi.

Její role v síti je nepostradatelná pro umožnění široké škály lokalizačních aplikací. Pro tísňové služby LSCF zajišťuje, že poloha volajícího je určena rychle a spolehlivě, často pomocí síťově iniciovaných žádostí s vysokou prioritou. Pro komerční služby poskytuje zabezpečenou, na soukromí ohleduplnou a standardizovanou bránu. LSCF abstrahuje složitost podkladové rádiové přístupové technologie (ať už jde o metody určování polohy v GSM, UMTS nebo LTE) před externím klientem a poskytuje jednotné rozhraní. To umožňuje poskytovatelům služeb žádat o polohu bez nutnosti detailní znalosti topologie sítě nebo lokalizačních technik, čímž se zjednodušuje vývoj a nasazení služeb.

## K čemu slouží

LSCF byla vytvořena, aby poskytla standardizovaný, centralizovaný řídicí bod pro lokalizační služby v rámci buněčných sítí. Před její standardizací byly lokalizační schopnosti často proprietární, řešení specifická pro dodavatele, která bylo obtížné integrovat s externími aplikacemi a která nemohla garantovat interoperabilitu napříč více-dodavatelskými sítěmi nebo pro roamující účastníky. LSCF řeší základní problém, jak koordinovat komplexní, vícekrokový proces zahrnující entity jádra sítě, zdroje rádiové přístupové sítě a externí klienty konzistentním a bezpečným způsobem.

Historicky byl hnací silou pro standardizaci LCS – a tedy i LSCF – dvojí požadavek: regulatorní nařízení pro lokalizaci tísňových volajících a tržní poptávka po komerčních lokalizačních službách. Regulátoři požadovali spolehlivý, síťový mechanismus pro lokalizaci tísňových volajících. To si vyžádalo řídicí funkci, která by mohla přepsat běžné procedury, upřednostnit zdroje a komunikovat se sítěmi tísňových služeb. Současně operátoři a poskytovatelé služeb třetích stran hledali společné API pro budování aplikací pro navigaci, sledování majetku a lokalizační informace. LSCF byla navržena tak, aby plnila obě role, poskytujíc jediný řídicí bod, který vynucuje soukromí, provádí autorizaci a spravuje technickou relaci.

Motivací pro její návrh bylo oddělení řídicí logiky od samotného výpočtu polohy. Tato modulární architektura umožňuje, aby se metody určování polohy (řešené SMLC/E-SMLC) vyvíjely nezávisle s novými rádiovými technologiemi (např. od Cell-ID přes OTDOA po NR positioning), zatímco řídicí a servisní logika v LSCF zůstává stabilnější. Řeší omezení dřívějších monolitických systémů definováním jasných referenčních bodů (rozhraní) mezi LSCF a dalšími síťovými funkcemi. To umožňuje operátorům získávat různé komponenty od různých dodavatelů a zajišťuje, že účastník může být lokalizován bez ohledu na to, zda je ve své domovské síti nebo roamuje, protože LSCF navštívené sítě (nebo GMLC, která ji obsahuje) může žádost zpracovat.

## Klíčové vlastnosti

- Funguje jako centrální řadič a koordinátor pro všechny žádosti o lokalizační služby v rámci PLMN.
- Ověřuje a autorizuje lokalizační žádosti vůči profilům soukromí účastníka a oprávněním klienta.
- Určuje obsluhující síťový uzel (MSC/MME/AMF) pro UE dotazem na HSS/HLR/UDM.
- Řídí lokalizační relaci s lokalizačním uzlem založeným v RAN (SMLC/E-SMLC/LMF).
- Poskytuje standardizované rozhraní (např. přes GMLC) pro externí LCS klienty pro žádosti o polohu.
- Spravuje překlad protokolů mezi externími aplikačními protokoly (např. MLP) a interními síťovými signalizačními protokoly.

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [MLP – Mobile Location Protocol](/mobilnisite/slovnik/mlp/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lscf/)
