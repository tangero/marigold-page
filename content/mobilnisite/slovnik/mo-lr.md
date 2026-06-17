---
slug: "mo-lr"
url: "/mobilnisite/slovnik/mo-lr/"
type: "slovnik"
title: "MO-LR – Mobile Originated Location Request"
date: 2026-01-01
abbr: "MO-LR"
fullName: "Mobile Originated Location Request"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mo-lr/"
summary: "MO-LR je funkce služby určování polohy (LCS), která umožňuje mobilnímu zařízení vyžádat si od sítě svou vlastní zeměpisnou polohu nebo polohu jiného cílového zařízení. Umožňuje uživateli iniciované ap"
---

MO-LR je funkce služby určování polohy, při které mobilní zařízení iniciuje žádost směrem k síti o získání své vlastní zeměpisné polohy nebo polohy jiného cílového zařízení.

## Popis

Mobile Originated Location Request (MO-LR) je procedura v rámci architektury služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) 3GPP, která umožňuje uživatelskému zařízení (UE) vystupovat jako LCS klient a iniciovat žádost o určení své vlastní polohy nebo polohy jiného specifikovaného cílového UE. Proces zahrnuje signalizaci mezi UE, obsluhující jádrovou sítí a funkcí správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) v 5G nebo Evolved Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE. UE odesílá žádost o polohu prostřednictvím vyhrazené zprávy protokolu LCS po řídicí rovině.

Po přijetí žádosti MO-LR síť autentizuje a autorizuje žádající UE na základě profilů účastníka. Pro žádost o vlastní polohu síť následně vyvolá příslušnou metodu určování polohy. Může se jednat o metodu založenou na síti (např. Observed Time Difference of Arrival - [OTDOA](/mobilnisite/slovnik/otdoa/) v LTE, Downlink Time Difference of Arrival - [DL-TDOA](/mobilnisite/slovnik/dl-tdoa/) v NR), na UE (s využitím asistenčních dat jako [GPS](/mobilnisite/slovnik/gps/)/[GNSS](/mobilnisite/slovnik/gnss/)) nebo o hybridní metody. Obsluhující uzel ([MME](/mobilnisite/slovnik/mme/)/AMF) koordinuje spolupráci se serverem pro určování polohy (E-SMLC/LMF), který vypočítá odhad polohy. Výsledná poloha (zeměpisná šířka, délka, přesnost) je pak doručena zpět žádajícímu UE v zprávě s odpovědí o poloze.

Pokud je žádost určena pro jiné cílové UE (s výhradou ověření soukromí), síť provede žádost o polohu vůči tomuto cíli (podobně jako u Mobile Terminated Location Request - MT-LR), získá polohu a předá ji původnímu UE. Mezi klíčové architektonické komponenty patří LCS klient v UE, protokol LCS ve vrstvě NAS, řídicí uzel jádrové sítě (MSC, SGSN, MME, AMF), server pro určování polohy (SMLC, E-SMLC, LMF) a rádiová přístupová síť, která poskytuje měřicí data (např. měření PRS pro OTDOA).

Úloha MO-LR v síti spočívá v podpoře uživatelsky orientovaných služeb založených na poloze (LBS). Umožňuje koncovému uživateli aktivně získávat informace o poloze, čímž se odlišuje od služeb určování polohy iniciovaných sítí nebo pro nouzové účely. Je základním prvkem pro komerční aplikace, neboť poskytuje standardizovaný mechanismus řídicí roviny pro zařízení, aby získala své vlastní souřadnice pro použití v mapování, sociálních sítích, sledování majetku a aplikacích rozšířené reality. Procedura zahrnuje ochranu soukromí a vyžaduje souhlas uživatele a kontrolu autorizace.

## K čemu slouží

MO-LR byl vyvinut za účelem standardizace metody, pomocí které mohou mobilní zařízení aktivně žádat síť o informace o poloze, což umožňuje širokou škálu uživateli řízených služeb založených na poloze. Před standardizovanými službami LCS byly možnosti určování polohy proprietární nebo omezené na služby iniciované sítí (např. pro zákonný odposlech). Vytvoření MO-LR reagovalo na rostoucí tržní poptávku po aplikacích, jako je navigace s pokyny po jednotlivých krocích, vyhledávání zohledňující polohu a sdílení polohy mezi osobami.

Řešil problém poskytnutí spolehlivého, bezpečného a operátorem řízeného mechanismu pro zařízení, aby získala přesnou polohu. Bez MO-LR by aplikace byly závislé pouze na vestavěném GPS, které má omezení v interiérech, v městských kaňonech a u zařízení bez hardwaru GPS. MO-LR využívá metody určování polohy založené na síti (např. Cell-ID, OTDOA) a asistovaného GNSS (A-GNSS) k poskytnutí rychlejšího, přesnějšího a energeticky efektivnějšího určení polohy než samostatné GPS.

Technologie byla motivována komerčním potenciálem služeb LBS a potřebou interoperability napříč zařízeními a sítěmi. Poskytla jakousi standardizovanou API v rámci síťové signalizace, což vývojářům aplikací umožnilo vytvářet služby s vědomím, že existuje konzistentní metoda pro získání polohy. Zavedla také nezbytné kontroly soukromí, které zajišťují, že polohu uživatele nemůže bez autorizace získat jiná strana, čímž vyvážila inovace služeb s ochranou účastníka.

## Klíčové vlastnosti

- Žádost iniciovaná UE: Mobilní zařízení zahajuje proceduru žádosti o polohu prostřednictvím standardizované signalizace řídicí roviny LCS.
- Podpora vlastní a polohy třetí strany: Může požadovat polohu žádajícího UE samotného nebo, s autorizací, polohu jiného cílového UE.
- Více metod určování polohy: Může využívat síťově asistovaný GNSS (A-GNSS), Observed Time Difference of Arrival (OTDOA), Enhanced Cell ID (E-CID) a další standardizované metody.
- Autorizace soukromí: Zahrnuje povinné ověření soukromí pro žádosti cílené na jiného účastníka, s účastí Home Subscriber Server (HSS) nebo registru profilů soukromí.
- Parametry QoS: Umožňuje žádajícímu UE specifikovat parametry kvality služby, jako je požadovaná přesnost a doba odezvy pro odhad polohy.
- Spolupráce s jádrovou sítí: Funguje napříč jádrovými sítěmi GSM, UMTS, LTE a 5G prostřednictvím obsluhujícího MSC, SGSN, MME nebo AMF, které komunikují s příslušným serverem pro určování polohy.

## Související pojmy

- [MT-LR – Mobile Terminated Location Request](/mobilnisite/slovnik/mt-lr/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 24.171** (Rel-19) — NAS Protocol for LCS in E-UTRAN
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 29.515** (Rel-19) — Ngmlc Service Based Interface Protocol
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [MO-LR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mo-lr/)
