---
slug: "lcss"
url: "/mobilnisite/slovnik/lcss/"
type: "slovnik"
title: "LCSS – LCS Server"
date: 2025-01-01
abbr: "LCSS"
fullName: "LCS Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcss/"
summary: "LCS Server je základní síťová entita, která zpracovává požadavky na polohové služby od LCS klientů. Řídí určování polohy, vynucuje ochranu soukromí a vrací odhady polohy, čímž funguje jako centrální ř"
---

LCSS je základní síťová entita, která zpracovává požadavky na polohové služby, řídí určování polohy, vynucuje ochranu soukromí a vrací odhady polohy pro polohové služby 3GPP.

## Popis

[LCS](/mobilnisite/slovnik/lcs/) Server je centrální funkční entita v architektuře polohových služeb (LCS) 3GPP odpovědná za zpracování, autorizaci a vyřizování žádostí o zeměpisnou polohu mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelského zařízení (UE). Logicky je implementován jako Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) v základní síti, ačkoli role LCSS může být v rozvinutých architekturách distribuována i do jiných uzlů. LCSS přijímá požadavek na polohovou službu od LCS klienta ([LCSC](/mobilnisite/slovnik/lcsc/)) prostřednictvím rozhraní jako Le (pro externí klienty) nebo interní signalizace. Po přijetí provádí několik klíčových funkcí: autentizuje žádajícího klienta, kontroluje jeho autorizaci pro požadovanou službu, ověřuje nastavení ochrany soukromí cílového účastníka a určuje vhodnou metodu určování polohy na základě požadované kvality služby (QoS).

LCSS poté funguje jako orchestrátor a komunikuje s příslušnými síťovými prvky za účelem získání odhadu polohy. Pro volání v přepojování okruhů typicky dotazuje Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)); pro relace v přepojování paketů kontaktuje Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)); a v sítích LTE/5G komunikuje s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function (AMF). Tyto navštívené síťové uzly mohou samy provést výpočet polohy pomocí síťových metod (např. Cell-ID, Uplink Time Difference of Arrival - U-TDOA) nebo koordinovat s UE pro metody s asistencí UE nebo založené na UE, jako je Assisted GNSS (A-GNSS) nebo Observed Time Difference of Arrival (OTDOA). Vypočtená polohová data jsou pak směrována zpět přes síťové prvky k LCSS.

Nakonec LCSS naformátuje odhad polohy (např. do popisů tvaru jako bod na elipsoidu s kruhem nejistoty) a vrátí jej žádajícímu LCSC. Zpracovává také generování účtovacích dat pro transakci polohové služby. Klíčovým architektonickým aspektem je oddělení mezi domácí sítí a navštívenou sítí. Home GMLC (H-GMLC) je prvním kontaktním bodem pro externího LCSC a řeší ochranu soukromí účastníka a směrování, zatímco Visited GMLC (V-GMLC) v obsluhující síti komunikuje s rádiovou přístupovou sítí za účelem získání skutečné polohy. Toto oddělení zajišťuje, že se nastavení ochrany soukromí účastníka, definovaná v Home Location Register (HLR) nebo Home Subscriber Server (HSS) domácí sítě, uplatní ještě předtím, než je jakýkoli požadavek na polohu přeposlán do obsluhující sítě.

## K čemu slouží

LCS Server byl vytvořen, aby poskytl standardizovaný, zabezpečený a škálovatelný řídicí bod pro polohové služby v sítích 3GPP. Před jeho definicí byla polohová funkčnost často ad-hoc doplňkem síťových prvků, kterému chyběla jednotná metodika pro autorizaci služeb, správu ochrany soukromí a interoperabilitu mezi operátory. Koncept LCSS centralizoval tyto klíčové řídicí funkce, což umožnilo komerční a regulatorní nasazení služeb založených na poloze.

Jeho primárním účelem je řešit problém kontrolovaného přístupu k polohovým informacím účastníka. Funguje jako důvěryhodný zprostředkovatel mezi subjekty žádajícími o polohu (LCSC) a možnostmi určování polohy v síti. Centralizací autentizace, autorizace a kontroly ochrany soukromí brání neoprávněnému přístupu a zajišťuje soulad s regulatorními požadavky, jako jsou ty pro tísňové služby (např. E911 v USA), a zákony na ochranu dat. Dále, díky abstrakci složitosti různých technologií rádiového přístupu (od GSM po 5G NR) a metod určování polohy, poskytuje klientům konzistentní servisní rozhraní. Tato abstrakce byla klíčová pro vývoj sítí, protože umožnila integrovat nové polohové technologie do sítě bez nutnosti změn servisní logiky externích poskytovatelů aplikací.

## Klíčové vlastnosti

- Autentizuje a autorizuje požadavky LCS klientů
- Vynucuje nastavení ochrany soukromí účastníka a regulatorní požadavky
- Řídí určování polohy dotazováním MSC, SGSN, MME nebo AMF
- Vybírá metodu určování polohy na základě požadované QoS (např. přesnost, latence)
- Formátuje a vrací odhady polohy (např. popisy tvaru) klientovi
- Generuje záznamy o účtování dat pro transakce polohové služby

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [LCSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcss/)
