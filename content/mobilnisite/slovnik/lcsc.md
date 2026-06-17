---
slug: "lcsc"
url: "/mobilnisite/slovnik/lcsc/"
type: "slovnik"
title: "LCSC – LCS Client"
date: 2025-01-01
abbr: "LCSC"
fullName: "LCS Client"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcsc/"
summary: "LCS Client je logická funkční entita, která vyžaduje polohové služby od sítě. Je klíčovou součástí architektury polohových služeb (LCS) dle 3GPP, umožňující aplikace jako tísňové služby, sledování voz"
---

LCSC je logická funkční entita v architektuře 3GPP LCS, která vyžaduje polohové služby od sítě pro aplikace, jako jsou tísňové služby nebo sledování vozového parku.

## Popis

[LCS](/mobilnisite/slovnik/lcs/) Client je základní entita v architektuře polohových služeb (LCS) dle 3GPP, definovaná jako logická role spíše než konkrétní fyzický uzel. Reprezentuje jakoukoli entitu, která požaduje polohu mobilní stanice ([MS](/mobilnisite/slovnik/ms/)), uživatelského zařízení (UE) nebo jiného cíle. LCSC iniciuje požadavek na určení polohy rozhraním se serverem LCS ([LCSS](/mobilnisite/slovnik/lcss/)) v síti. Požadavek obsahuje parametry jako identita cíle (např. [MSISDN](/mobilnisite/slovnik/msisdn/), [IMSI](/mobilnisite/slovnik/imsi/)), požadovaná kvalita služby (QoS) pro odhad polohy (např. přesnost, doba odezvy) a typ požadovaných polohových informací (např. aktuální poloha, periodické aktualizace). LCSC může sídlit na různých místech v síti: může jím být externí aplikační server (např. poskytovatel služeb s přidanou hodnotou), uzel uvnitř jádra sítě (např. pro zákonný odposlech nebo tísňové služby), nebo dokonce i uvnitř samotného UE pro určení polohy iniciované účastníkem.

Architektonicky LCSC komunikuje s LCS Serverem přes standardizovaná rozhraní, primárně referenční bod Le pro externí klienty a LCS Application Protocol ([LCS-AP](/mobilnisite/slovnik/lcs-ap/)) pro interní síťové klienty. LCSS funguje jako brána a procesor těchto požadavků, autentizuje klienta, autorizuje požadavek na určení polohy a řídí proces určování polohy s příslušnými síťovými elementy, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) nebo evolved NodeB (eNB). Jakmile je výpočet polohy dokončen (pomocí metod jako Cell-ID, OTDOA nebo A-GNSS), LCSS vrátí odhad polohy a přidružené údaje o přesnosti žádajícímu LCSC.

Role LCSC je klíčová pro umožnění široké škály polohově závislých služeb (LBS). Abstrahuje složité síťové mechanismy určování polohy a poskytuje standardizované služební rozhraní. LCSC jsou kategorizovány na základě vztahu k operátorovi sítě: klienti služeb s přidanou hodnotou (VAS) jsou externí třetí strany, klienti síťového operátora jsou interní (např. pro operace nebo tísňová volání) a klienti založení na UE pocházejí ze samotného zařízení. Tato kategorizace ovlivňuje použité postupy autentizace, účtování a ochrany soukromí pro požadavek na určení polohy. Funkcionalita LCSC zajišťuje, že polohové informace mohou být bezpečně a spolehlivě doručeny autorizovaným subjektům, čímž tvoří služební koncový bod pro celý LCS systém.

## K čemu slouží

Entita LCS Client byla zavedena za účelem standardizace rozhraní pro vyžadování polohových informací mobilních zařízení, což je schopnost, která se stala nezbytnou s rozšířením celulárních sítí. Před standardizací 3GPP existovaly proprietární metody pro polohové služby, které bránily interoperabilitě a rozvoji širokého ekosystému polohově závislých aplikací. Vytvoření entity LCSC řešilo potřebu jasného, bezpečného a řízeného vstupního bodu pro požadavky na polohové služby, oddělující služební logiku od podkladových technologií určování polohy v rádiovém přístupu a jádru sítě.

Její zavedení vyřešilo několik klíčových problémů. Za prvé umožnilo poskytovatelům služeb třetích stran (služby s přidanou hodnotou) přistupovat k síťovým polohovým datům přes standardizované, zpoplatněné rozhraní (Le), čímž podpořilo inovace v oblastech jako navigace, sledování majetku nebo polohově cílená reklama. Za druhé poskytlo mechanismus pro síťově interní služby, jako je směrování tísňových hovorů (E911/E112) nebo zákonný odposlech, pro spolehlivé získání polohy účastníka. Nakonec, definováním typů klientů a přidružených profilů soukromí, vytvořilo rámec pro ochranu soukromí účastníků, zajišťující, že polohové informace jsou zpřístupňovány pouze v souladu se souhlasem účastníka a regulatorními požadavky. Koncept LCSC byl tedy zásadní pro transformaci mobilních sítí z čistě komunikačních platforem na technologie umožňující kontextové, polohově závislé služby.

## Klíčové vlastnosti

- Iniciuje standardizované požadavky na polohové služby vůči LCS Serveru
- Podporuje více typů klientů: Služby s přidanou hodnotou (externí), Síťový operátor (interní) a založené na UE
- Specifikuje parametry požadavku na určení polohy včetně identity cíle, QoS (přesnost, doba odezvy) a typu polohy
- Komunikuje přes referenční bod Le pro externí klienty nebo interní protokoly pro síťové klienty
- Podléhá procedurám autentizace, autorizace a účtování
- Řídí se kontrolami ochrany soukromí a zabezpečení definovanými architekturou LCS

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [LCSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcsc/)
