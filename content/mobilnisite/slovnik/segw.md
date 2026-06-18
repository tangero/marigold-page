---
slug: "segw"
url: "/mobilnisite/slovnik/segw/"
type: "slovnik"
title: "SEGW – Security Gateway"
date: 2025-01-01
abbr: "SEGW"
fullName: "Security Gateway"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/segw/"
summary: "Síťový uzel, který poskytuje zabezpečené IPsec tunelování pro řídicí a uživatelskou rovinu mezi sítěmi 3GPP a ne-3GPP. Je klíčový pro ochranu mezisíťové komunikace, zejména pro důvěryhodný ne-3GPP pří"
---

SEGW je síťový uzel, který zajišťuje zabezpečené IPsec tunelování pro řídicí a uživatelskou rovinu mezi sítěmi 3GPP a ne-3GPP, čímž chrání komunikaci mezi sítěmi.

## Popis

Bezpečnostní brána (SEGW) je klíčová funkční entita definovaná v architektuře 3GPP, primárně pro zabezpečení konektivity mezi jádrovou sítí 3GPP (jako Evolved Packet Core nebo 5G Core) a externími IP sítěmi ne-3GPP. Funguje jako koncový bod pro [IPsec](/mobilnisite/slovnik/ipsec/) (Internet Protocol Security) tunely, které jsou navázány mezi uživatelským zařízením (UE) nebo externím síťovým uzlem a samotnou SEGW. Primární role SEGW spočívá v autentizaci vzdáleného koncového bodu, vyjednávání bezpečnostních asociací pomocí protokolů jako IKEv2 (Internet Key Exchange version 2) a vynucování bezpečnostních politik pro šifrovaný provoz procházející tunelem.

Architektonicky je SEGW často nasazena na okraji důvěryhodné domény operátora. Pro scénáře jako důvěryhodný ne-3GPP přístup (např. propojení s Wi-Fi) naváže UE IPsec tunel přímo s SEGW. Tento tunel zapouzdří veškerý provoz určený pro jádro 3GPP a chrání jej při průchodu nedůvěryhodnou sítí ne-3GPP. SEGW následně provoz dešifruje a přepošle jej příslušným funkcím jádrové sítě, jako je Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPC nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC. Slouží jako bezpečnostní kotva, skrývající vnitřní topologii jádrové sítě a poskytující první linii obrany.

Provoz SEGW zahrnuje několik klíčových komponent a procedur. Udržuje databáze bezpečnostních politik, které definují povolené selektory provozu a používané kryptografické algoritmy. Během navazování tunelu provádí vzájemnou autentizaci s UE, často pomocí EAP-AKA nebo certifikátů. Jakmile je bezpečnostní asociace ([SA](/mobilnisite/slovnik/sa/)) IPsec navázána, SEGW zpracovává šifrování/dešifrování paketů a volitelně plní funkce pro překlad síťových adres ([NAT](/mobilnisite/slovnik/nat/)). Její role je odlišná, ale může být kolidována s jinými bránovými funkcemi, jako je ePDG (evolved Packet Data Gateway), což je specifický typ SEGW pro nedůvěryhodný ne-3GPP přístup.

V širším síťovém ekosystému je SEGW nezbytná pro umožnění zabezpečeného podnikového přístupu, nasazení IoT (jako jsou ta definovaná pro kritickou komunikaci) a bezproblémové mobility mezi 3GPP a ne-3GPP rádiovými technologiemi. Zajišťuje, že důvěrnost, integrita a často i ochrana proti opakování jsou zachovány pro provoz vstupující do domény operátora z externích sítí, čímž tvoří základní prvek architektury zabezpečení 3GPP pro heterogenní přístup.

## K čemu slouží

SEGW byla zavedena, aby řešila rostoucí potřebu zabezpečeného propojení mezi mobilními sítěmi 3GPP a externími IP sítěmi, zejména když operátoři začali integrovat přístupové technologie ne-3GPP jako Wi-Fi. Před její standardizací bylo zabezpečení takových propojení často řešeno proprietárními řešeními nebo obecnými firewally, kterým chyběla jednotná, interoperabilní metoda pro navazování důvěryhodných, šifrovaných tunelů s mobilními zařízeními. SEGW poskytuje standardizovaný mechanismus pro rozšíření bezpečnostního perimetru mobilní jádrové sítě.

Primární problém, který řeší, je ochrana provozu řídicí a uživatelské roviny při průchodu potenciálně nedůvěryhodnými sítěmi. Například když se uživatel připojí přes veřejný Wi-Fi hotspot, je provoz mezi jeho zařízením a mobilním jádrem zranitelný vůči odposlechu a manipulaci. SEGW ve spolupráci s UE vytvoří zabezpečený [IPsec](/mobilnisite/slovnik/ipsec/) tunel, čímž efektivně promění nedůvěryhodný přístupový spoj v virtuální propojení do důvěryhodné domény operátora. To bylo klíčovým prvkem pro standardy jako [GAN](/mobilnisite/slovnik/gan/) (Generic Access Network) a později pro důvěryhodný a nedůvěryhodný ne-3GPP přístup do EPC a 5GC.

Historicky byl její vývoj motivován prací 3GPP na evoluci systémové architektury a konvergenci pevných a mobilních sítí. Specifikace jako 43.318 (pro GAN) a později 23.402 (pro vylepšení architektury pro ne-3GPP přístup) formalizovaly její roli. SEGW umožňuje operátorům nabízet bezproblémové a bezpečné služby bez ohledu na podkladovou přístupovou technologii, což je základním kamenem pro poskytování konzistentní kvality uživatelského zážitku a zabezpečení v dnešních sítích s více přístupy.

## Klíčové vlastnosti

- Koncový bod pro IPsec tunely (IKEv2/IPsec)
- Vzájemná autentizace koncových bodů tunelu pomocí EAP nebo certifikátů
- Vynucování bezpečnostních politik pro šifrovaný provoz
- Podpora mechanismů pro překlad síťových adres (NAT traversal)
- Může sloužit jako bezpečnostní kotva pro důvěryhodný ne-3GPP přístup
- Spolupracuje s funkcemi jádrové sítě (PGW, UPF) pro přeposílání uživatelské roviny

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)

## Definující specifikace

- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [SEGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/segw/)
