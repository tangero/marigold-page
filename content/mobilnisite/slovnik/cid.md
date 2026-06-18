---
slug: "cid"
url: "/mobilnisite/slovnik/cid/"
type: "slovnik"
title: "CID – Cell-ID Positioning Method"
date: 2025-01-01
abbr: "CID"
fullName: "Cell-ID Positioning Method"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cid/"
summary: "CID je síťová metoda určování polohy, která identifikuje polohu mobilního zařízení na základě geografické pokrytí obslužné buňky. Poskytuje nejjednodušší formu lokalizace v mobilních sítích tím, že as"
---

CID je síťová metoda určování polohy, která identifikuje polohu mobilního zařízení na základě geografické oblasti jeho obslužné buňky.

## Popis

Metoda určování polohy Cell-ID (CID) funguje jako základní technika lokalizace v sítích 3GPP tím, že využívá znalost poloh základnových stanic stávající buněčné infrastruktury. Když se mobilní zařízení připojí k síti, registruje se u konkrétní buňky identifikované jedinečnou identitou Cell Global Identity ([CGI](/mobilnisite/slovnik/cgi/)), která zahrnuje Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)), Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)), Location Area Code ([LAC](/mobilnisite/slovnik/lac/)) a Cell Identity ([CI](/mobilnisite/slovnik/ci/)). Polohová architektura sítě, včetně Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) a Serving Mobile Location Centre ([SMLC](/mobilnisite/slovnik/smlc/)), načte tuto informaci o buňce z Radio Access Network (RAN) a namapuje ji na geografické souřadnice uložené v databázi buněk sítě.

Technicky funguje určování polohy CID prostřednictvím vícekrokového procesu, který je zahájen při příchodu požadavku na polohu do GMLC od externího klienta služby založené na poloze (Location-Based Service, [LBS](/mobilnisite/slovnik/lbs/)). GMLC identifikuje příslušný SMLC nebo Mobility Management Entity (MME) obsluhující cílové zařízení, který následně dotazuje aktuální informaci o obslužné buňce od základnové stanice (NodeB, eNodeB nebo gNB). Síť načte geografické souřadnice buňky (zeměpisná šířka, délka) a poloměr pokrytí ze své buněčné databáze, která obsahuje předkonfigurované informace o všech nasazených buňkách. Výsledek určení polohy je vrácen jako odhadovaná pozice s poloměrem nejistoty rovným pokrytí buňky, typicky v rozsahu od stovek metrů v hustých městských oblastech až po několik kilometrů ve venkovském prostředí.

Přesnost metody CID zcela závisí na velikosti buňky a hustotě nasazení, přičemž menší buňky poskytují lepší přesnost lokalizace. V sítích 5G se metoda CID integruje s Location Management Function (LMF) a Access and Mobility Management Function (AMF) pro poskytování lokalizačních služeb napříč různými Radio Access Technologies (RAT). Metoda podporuje jak řídicí (control-plane), tak uživatelskou (user-plane) polohovou architekturu, přičemž 3GPP TS 23.271 a TS 36.305 specifikují signalizační postupy a požadavky. Zatímco samostatné CID poskytuje základní lokalizaci, často slouží jako výchozí fixace pro pokročilejší techniky, jako je Observed Time Difference of Arrival (OTDOA) nebo Assisted GNSS (A-GNSS), když tyto metody selžou nebo vyžadují dodatečný čas pro výpočet.

Klíčové architektonické komponenty zahrnují databázi buněk obsahující geografické informace pro všechny síťové buňky, polohové protokoly (LPP, LPPa, NRPPa), které přenášejí polohová měření a asistenční data, a síťové entity koordinující požadavky na určení polohy. CID vyžaduje minimální signalizační režii ve srovnání s jinými metodami, protože využívá stávající postupy připojení k buňce namísto vyžadování dodatečných měření. Jednoduchost metody zajišťuje její univerzální dostupnost napříč všemi releasy 3GPP a typy zařízení, funguje dokonce i s legacy User Equipment (UE), které postrádají polohové schopnosti, ačkoli omezení přesnosti omezují její použití na aplikace, kde postačuje přibližná poloha.

## K čemu slouží

Určování polohy CID bylo zavedeno ve 3GPP Release 5, aby splnilo regulatorní požadavky na lokalizaci nouzových volajících (E911 v USA, E112 v Evropě) a zároveň poskytlo univerzálně dostupné, nákladově efektivní polohové řešení. Před CID mobilní sítě postrádaly standardizované metody určování polohy, což činilo služby založené na poloze závislé na proprietárních řešeních nebo externích GPS přijímačích. Metoda řešila kritickou potřebu základních lokalizačních schopností, které by mohly fungovat se stávající síťovou infrastrukturou a všemi mobilními zařízeními bez nutnosti hardwarových upgradů nebo dodatečných rádiových měření.

Primární motivací pro vývoj CID bylo vytvořit minimální základní lokalizační schopnost, kterou lze rychle nasadit ve všech sítích. Pokročilé metody určování polohy, jako OTDOA a A-GNSS, vyžadují významné síťové upgrady, schopnosti zařízení a čas na zpracování měření. CID poskytlo okamžitou lokalizační funkčnost využívající stávající data plánování buněk a standardní síťové postupy. To bylo zvláště důležité pro záchranné služby, kde jakákoli informace o poloze – dokonce i s nejistotou na úrovni kilometrů – byla pro první respondenty cenná ve srovnání s úplnou absencí polohových dat.

CID také umožnilo raný vývoj komerčních služeb založených na poloze tím, že poskytlo jednoduché API pro vývojáře aplikací. Přestože omezení přesnosti omezovalo případy užití na služby počasí, lokalizaci obsahu a základní sledovací aplikace, demonstrovalo to potenciál buněčné lokalizace. Síťový přístup metody znamenal, že poskytovatelé služeb mohli nabízet lokalizační služby bez závislosti na schopnostech koncových zařízení, čímž vytvářeli příležitosti pro příjmy a zároveň budovali cestu k přesnějším polohovým metodám v následujících releasech. CID vytvořilo základní architekturu a signalizační postupy, které se později vyvinuly pro podporu hybridního určování polohy kombinujícího více technik.

## Klíčové vlastnosti

- Síťové určování polohy nevyžadující úpravy zařízení
- Využívá stávající postupy a signalizaci připojení k buňce
- Poskytuje polohu jako centroid buňky s nejistotou danou poloměrem pokrytí
- Funguje napříč všemi releasy 3GPP a Radio Access Technologies
- Podporuje jak řídicí (control-plane), tak uživatelskou (user-plane) architekturu
- Slouží jako záložní řešení, když pokročilé metody určování polohy selžou

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 33.814** (Rel-16) — Security aspects of enhanced Location Services (eLCS)
- **TS 33.831** (Rel-12) — Study on Spoofed Call Detection & Prevention
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [CID na 3GPP Explorer](https://3gpp-explorer.com/glossary/cid/)
