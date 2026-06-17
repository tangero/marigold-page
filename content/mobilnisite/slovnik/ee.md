---
slug: "ee"
url: "/mobilnisite/slovnik/ee/"
type: "slovnik"
title: "EE – Energy Efficiency"
date: 2026-01-01
abbr: "EE"
fullName: "Energy Efficiency"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ee/"
summary: "Rámec pro měření, reportování a zlepšování spotřeby energie v sítích 3GPP. Definuje metriky, modely a požadavky pro snížení provozních nákladů a dopadu na životní prostředí. Je klíčový pro udržitelný"
---

EE je 3GPP rámec pro měření, reportování a zlepšování spotřeby energie v síti za účelem snížení provozních nákladů a dopadu na životní prostředí.

## Popis

Energy Efficiency (EE) v 3GPP je komplexní rámec zahrnující metodologie, metriky a požadavky navržené pro vyhodnocení a zlepšení energetické výkonnosti mobilních sítí. Působí napříč více doménami, včetně rádiové přístupové sítě (RAN), core sítě a koncových uživatelských zařízení. Rámec stanovuje standardizované metriky energetické účinnosti (EEMs) a vyhodnocovací metodologie (EEMeth), které umožňují konzistentní měření a porovnání spotřeby energie za definovaných scénářů provozní zátěže a nasazení. Tyto metriky jsou klíčové pro operátory, aby mohli benchmarkovat výkonnost, identifikovat neefektivity a ověřovat tvrzení dodavatelů zařízení o úsporách energie.

Architektura ohledů na EE je integrována do plánování, nasazování a provozu sítě. Mezi klíčové technické komponenty patří modely spotřeby energie pro síťové prvky (např. základnové stanice, funkce core sítě), strategie režimu spánku pro rádiová zařízení během období nízkého provozu a techniky optimalizace spotřeby energie sítě. Specifikace podrobně popisují, jak měřit spotřebu energie pro lokality základnových stanic (včetně rádiové části, zpracování a chlazení) a definují energetickou účinnost na úrovni sítě jako poměr celkového přeneseného datového provozu k celkové energii spotřebované sítí. Rámec také pokrývá energetickou účinnost uživatelského zařízení (UE), stanovuje požadavky na spotřebu energie v různých provozních stavech.

Role EE zasahuje do správy sítě prostřednictvím definice funkcí Energy Saving Management ([ESM](/mobilnisite/slovnik/esm/)). Ty jsou součástí širšího Network Management System ([NMS](/mobilnisite/slovnik/nms/)) a Element Management System ([EMS](/mobilnisite/slovnik/ems/)) a umožňují aktivaci a deaktivaci funkcí pro úsporu energie na základě politiky a stavu sítě. Specifikace poskytují podrobné procedury pro úsporu energie na úrovni buňky, sektoru a nosné, často zahrnující dynamické vypínání hardwarových komponent nebo celých nosných, když je poptávka po kapacitě nízká. To vyžaduje pečlivou koordinaci pro zachování kvality služeb a pokrytí, což činí EE kritickým aspektem moderních operací Self-Organizing Network (SON) a automatizované správy sítě.

## K čemu slouží

Vytvoření rámce 3GPP pro energetickou účinnost bylo motivováno rychle rostoucí spotřebou energie a provozními výdaji ([OPEX](/mobilnisite/slovnik/opex/)) mobilních sítí, poháněnými prudce rostoucím datovým provozem a zhušťováním sítě. Před jeho standardizací byly techniky úspory energie proprietární jednotlivých dodavatelů, což operátorům ztěžovalo porovnávání řešení nebo měření celkové výkonnosti sítě. Nebyl žádný společný základ pro definování nebo reportování energetické účinnosti, což bránilo celoprůmyslovému pokroku směrem k cílům udržitelnosti. Rámec byl zaveden, aby poskytl standardizovaný, transparentní a měřitelný přístup ke snižování uhlíkové stopy a nákladů na elektřinu v celulárních sítích.

Historicky síťový design upřednostňoval výkonnost, kapacitu a pokrytí, přičemž spotřeba energie byla často považována za sekundární omezení. Jak získaly na významu obavy o životní prostředí, společenskou odpovědnost a řízení ([ESG](/mobilnisite/slovnik/esg/)) a ceny energie se staly volatilnějšími, průmysl uznal potřebu koordinovaného úsilí. Pracovní položka EE, zavedená ve Release 13, si kladla za cíl toto řešit vývojem technických specifikací, které umožňují energeticky účinné nasazení a provoz sítě. Řeší problém nekonzistentního měření definováním jasných klíčových ukazatelů výkonnosti (KPIs) a testovacích metodologií, což umožňuje spravedlivé hodnocení a podporuje inovace v technologiích pro úsporu energie v celém ekosystému.

## Klíčové vlastnosti

- Standardizované metriky energetické účinnosti (EEMs) pro síť a zařízení
- Definovaná vyhodnocovací metodologie (EEMeth) pro konzistentní měření a reportování
- Modely spotřeby energie pro základnové stanice a síťové prvky
- Specifikace funkcí a rozhraní Energy Saving Management (ESM)
- Požadavky na energetickou účinnost UE a výdrž baterie
- Podpora dynamické optimalizace spotřeby energie sítě a režimů spánku

## Související pojmy

- [ESM – Energy Savings Management](/mobilnisite/slovnik/esm/)
- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TR 21.866** (Rel-15) — Study on Energy Efficiency in 3GPP Standards
- **TR 22.882** (Rel-19) — Study on Energy Efficiency as a Service Criteria
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 28.310** (Rel-19) — Energy Efficiency Management for 5G Networks
- **TS 28.554** (Rel-20) — 5G Network & Slice KPI Specification
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 32.450** (Rel-19) — E-UTRAN Key Performance Indicators (KPI) Definitions
- **TS 32.451** (Rel-19) — KPI Requirements for E-UTRAN
- **TS 32.856** (Rel-15) — Energy Efficiency Assessment for RAN OAM
- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR
- **TR 38.913** (Rel-19) — Next Gen Access Tech Scenarios & Requirements
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [EE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ee/)
