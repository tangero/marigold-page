---
slug: "3g-msc"
url: "/mobilnisite/slovnik/3g-msc/"
type: "slovnik"
title: "3G-MSC – 3rd Generation Mobile Switching Centre"
date: 2025-01-01
abbr: "3G-MSC"
fullName: "3rd Generation Mobile Switching Centre"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/3g-msc/"
summary: "3G-MSC je centrální komutační uzel pro okruhově přepínané hlasové a datové služby v sítích 3G UMTS. Spravuje řízení hovorů, správu mobility a propojení s dalšími sítěmi, jako je PSTN. Byl klíčový pro"
---

3G-MSC je centrální komutační uzel v sítích 3G UMTS, který spravuje okruhově přepínané hlasové a datové služby, včetně řízení hovorů, správy mobility a propojení s dalšími sítěmi.

## Popis

3rd Generation Mobile Switching Centre (3G-MSC) je prvek jádra sítě definovaný v architektuře 3GPP UMTS, konkrétně pro okruhově přepínanou ([CS](/mobilnisite/slovnik/cs/)) doménu. Vyvinul se z 2G GSM Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)), aby zvládl požadavky systému 3G Universal Mobile Telecommunications System (UMTS). Architektonicky se nachází v rámci Core Network (CN) a rozhraní s UMTS Terrestrial Radio Access Network (UTRAN) přes rozhraní Iu-CS. Toto rozhraní přenáší uživatelskou rovinu (např. hlas kódovaný pomocí kodeků [AMR](/mobilnisite/slovnik/amr/)) a signalizaci řídicí roviny pro okruhově přepínané služby. 3G-MSC je zodpovědný za celý životní cyklus okruhově přepínaného hovoru, včetně jeho navázání, správy a ukončení. Provádí klíčové funkce, jako je analýza číslic, směrování, generování účtovacích dat a spolupráce s dalšími MSC nebo externími sítěmi, jako je Public Switched Telephone Network (PSTN) nebo Integrated Services Digital Network ([ISDN](/mobilnisite/slovnik/isdn/)). Klíčovou součástí v rámci 3G-MSC je Visitor Location Register (VLR), který je typicky umístěn společně s ním. VLR ukládá dočasná data účastníka (jako je lokalizační oblast a profil služeb) pro všechny mobilní stanice aktuálně nacházející se v geografické oblasti řízené MSC. Tato integrace umožňuje MSC rychlý přístup k informacím potřebným pro zpracování hovorů a správu mobility bez neustálého dotazování Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Pro mobilitu 3G-MSC zpracovává aktualizace lokalizační oblasti a je kotvícím bodem pro předávání spojení (handover) v rámci své servisní oblasti a k jiným MSC. Spravuje jak intra-MSC, tak inter-MSC handovery, čímž zajišťuje kontinuitu služeb při pohybu uživatele. V kontextu zabezpečení 3G-MSC spolupracuje s Authentication Centre (AuC) přes HLR k autentizaci účastníků a správě šifrování pro CS doménu. Má také rozhraní k Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)) pro validaci zařízení. Role 3G-MSC se s příchodem 3G rozšířila o podporu nových služeb umožněných vyšší šířkou pásma, jako je videotelefonie, přičemž jeho hlavní funkce zůstala zaměřená na spolehlivé okruhově přepínané spojení s nízkou latencí.

## K čemu slouží

3G-MSC byl vytvořen jako základní prvek okruhově přepínané části jádra sítě v 3G UMTS, aby zajistil zpětnou kompatibilitu a plynulou migraci ze sítí 2G GSM. Zatímco 3G přineslo nové rádiové rozhraní (WCDMA) a paketově přepínanou doménu pro data, hlas zůstal primární službou vyžadující spolehlivost a kvalitu okruhového přepojování. 3G-MSC vyřešil problém integrace nového UTRAN s existující infrastrukturou jádra sítě, což umožnilo operátorům využít své investice do GSM jader sítí při modernizaci jejich rádiového přístupu. Odstranil omezení 2G [MSC](/mobilnisite/slovnik/msc/) tím, že byl navržen pro zpracování specifických signalizačních protokolů (např. RANAP přes Iu-CS) a charakteristik provozu UMTS, s podporou vyšší kapacity a nových scénářů mobility zavedených s UTRAN. Historicky byl jeho vývoj v 3GPP Release 99 motivován potřebou jasné evoluční cesty z GSM. Bez vyhrazeného 3G-MSC by operátoři čelili významným výzvám při nasazování 3G služeb, protože standardní 2G MSC by nebylo optimalizováno pro rozhraní Iu nebo potenciálně odlišné vzorce provozu a procedury předávání spojení v síti založené na WCDMA. Zajistil, že základní telefonní služby zůstaly robustní, zatímco sítě se vyvíjely směrem k podpoře multimédií.

## Klíčové vlastnosti

- Řízení okruhově přepínaných hovorů pro hlas a videotelefonii
- Správa mobility pro aktualizaci polohy a provádění předání spojení (handover)
- Integrace s Visitor Location Register (VLR) pro správu dat účastníků
- Rozhraní s UTRAN přes rozhraní Iu-CS s využitím protokolu RANAP
- Funkce pro spolupráci (interworking) pro připojení k PSTN/ISDN a jiným PLMN
- Generování záznamů o účtovacích datech pro účely fakturace

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN

---

📖 **Anglický originál a plná specifikace:** [3G-MSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/3g-msc/)
