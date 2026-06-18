---
slug: "cmm"
url: "/mobilnisite/slovnik/cmm/"
type: "slovnik"
title: "CMM – Circuit Mobility Management"
date: 2025-01-01
abbr: "CMM"
fullName: "Circuit Mobility Management"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cmm/"
summary: "Circuit Mobility Management (CMM) je protokol 3GPP odpovědný za správu mobility a sledování polohy mobilních zařízení v sítích s přepojováním okruhů. Řeší procedury jako aktualizace polohy, předávání"
---

CMM je protokol 3GPP, který spravuje mobilitu a sledování polohy mobilních zařízení v sítích s přepojováním okruhů, jako jsou GSM a UMTS, a řeší aktualizace polohy, předávání hovorů a autentizaci.

## Popis

Circuit Mobility Management (CMM) je základní protokolová vrstva v architektuře 3GPP, speciálně navržená pro správu mobility uživatelského zařízení (UE) v doménách s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) sítí GSM a UMTS. Funguje jako část podsložky Mobility Management ([MM](/mobilnisite/slovnik/mm/)), která se nachází nad vrstvou Radio Resource ([RR](/mobilnisite/slovnik/rr/)) a pod vrstvou Connection Management ([CM](/mobilnisite/slovnik/cm/)) v protokolovém zásobníku. Primární funkcí CMM je udržovat přehled o poloze UE na detailní úrovni (Location Area nebo Routing Area), aby umožnilo efektivní doručování hovorů, a spravovat procedury vyžadované při pohybu UE mezi různými pokrytými oblastmi sítě.

Protokol funguje prostřednictvím řady dobře definovaných procedur iniciovaných buď sítí, nebo mobilním zařízením. Klíčové procedury zahrnují Location Updating (normální, periodické a [IMSI](/mobilnisite/slovnik/imsi/) attach/detach), které umožňují Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) sítě sledovat aktuální obsluhovanou oblast UE. Autentizační a šifrovací procedury jsou také iniciovány vrstvou CMM za účelem ověření identity účastníka a zabezpečení rádiového spoje. Dále CMM spravuje přípravu a provedení předání hovoru na síťové úrovni a koordinuje s vrstvou RR ohledně rádiových aspektů, když se UE během aktivního hovoru pohybuje mezi buňkami.

Z architektonického hlediska je funkčnost CMM distribuována mezi UE a jádrovou síť, konkrétně Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a s ním asociovaný VLR. Entita CMM v UE komunikuje s entitou CMM sítě pomocí specifických MM zpráv přes rádiové rozhraní. Stavový automat protokolu v UE může být ve stavech jako MM IDLE (žádné MM spojení), MM WAIT-FOR-NETWORK-COMMAND nebo MM CONNECTION-ACTIVE. Síť používá v procedurách CMM jako klíčové identifikátory International Mobile Subscriber Identity (IMSI) nebo Temporary Mobile Subscriber Identity (TMSI).

Role CMM je klíčová pro základní fungování sítí 2G a 3G. Zajišťuje, že jádrová síť s přepojováním okruhů může vždy směrovat příchozí hlasové hovory na správný MSC a základnovou stanici, která účastníka obsluhuje. Spravuje signalizační zátěž související s mobilitou v síti definováním různých typů aktualizací a časovačů. Ačkoli byl z velké části nahrazen GPRS Mobility Management (GMM) a později Evolved Packet System Mobility Management (EMM) pro paketové služby, CMM zůstal základním kamenem pro správu mobility hlasových služeb v legacy sítích, rozhraním s protokoly řízení hovoru pro navázání a udržení spojení s přepojováním okruhů.

## K čemu slouží

CMM byl vytvořen, aby vyřešil základní výzvu udržení kontinuity služeb pro mobilní účastníky využívající služby s přepojováním okruhů, primárně hlasové hovory, při jejich pohybu po buněčné síti. Před standardizovanými buněčnými systémy byla mobilní telefonie geograficky omezená. CMM jako součást standardů GSM zavedl systematickou, síťově řízenou metodu pro sledování polohy účastníka a správu procesu předávání hovorů mezi buňkami, což umožnilo skutečnou mobilitu na velkých územích.

Tato technologie řeší problém efektivního vyhledání účastníka pro mobilně ukončené hovory bez vyžadování nadměrného signalizačního provozu. Dosahuje toho rozdělením sítě na Location Areas a vyžadováním hlášení polohy od UE pouze při překročení hranice oblasti nebo v periodických intervalech. Tím vyvažuje potřebu znalosti sítě s úsporou rádiových zdrojů a baterie. Dále CMM integruje bezpečnostní procedury jako autentizaci, která chrání proti podvodům, a šifrování, které chrání soukromí uživatele na rádiovém spoji.

Historicky byl CMM základním kamenem úspěchu systému GSM, poskytujíc spolehlivou správu mobility, která umožnila masové rozšíření buněčných hlasových služeb. Stanovil model síťově řízené mobility s jasným oddělením mezi správou mobility (CMM), správou rádiových zdrojů (RR) a řízením hovoru (CM). Tento vrstvený přístup se stal vzorem pro pozdější systémy 3GPP. Jeho vytvoření bylo motivováno potřebou standardizované, robustní a škálovatelné metody pro správu milionů pohybujících se účastníků, což byl problém, který dřívější analogové systémy řešily s menší efektivitou a bezpečností.

## Klíčové vlastnosti

- Spravuje procedury Location Updating (Normální, Periodické, IMSI Attach/Detach) pro doménu s přepojováním okruhů
- Řeší autentizaci účastníka a iniciuje nastavení režimu šifrování pro zabezpečenou komunikaci
- Spravuje přidělování a přepřidělování Temporary Mobile Subscriber Identities (TMSI) pro soukromí účastníka
- Řídí navazování a uvolňování MM spojení mezi UE a sítí pro CS služby
- Koordinuje s vrstvou Radio Resource pro síťově asistovanou přípravu a provedení předání hovoru
- Udržuje MM-specifické časovače a stavy protokolu (IDLE, WAIT, CONNECTED) v UE a síti

## Související pojmy

- [GMM – Global Multimedia Mobility](/mobilnisite/slovnik/gmm/)
- [EMM – Evolved Mobility Management](/mobilnisite/slovnik/emm/)
- [TMSI – Temporary Mobile Subscriber Identifier](/mobilnisite/slovnik/tmsi/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [CMM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmm/)
