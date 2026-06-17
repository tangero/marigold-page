---
slug: "bmw"
url: "/mobilnisite/slovnik/bmw/"
type: "slovnik"
title: "BMW – Bayerische Motoren Werke"
date: 2025-01-01
abbr: "BMW"
fullName: "Bayerische Motoren Werke"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bmw/"
summary: "BMW je německý výrobce automobilů odkazovaný v technických specifikacích 3GPP jako příklad výrobce vozidel (Original Equipment Manufacturer – OEM). Je používán v technických studiích a normativním tex"
---

BMW je německý výrobce automobilů, který je v technických specifikacích 3GPP používán jako příklad výrobce vozidel (OEM) pro ilustraci požadavků na komunikaci vozidlo-se-vším (V2X).

## Popis

V rámci technických specifikací 3GPP, konkrétně v dokumentu TS 26.938, je 'Bayerische Motoren Werke' (BMW) uváděna nikoliv jako standardizovaný protokol nebo síťová funkce, ale jako reálný příklad automobilového výrobce (Original Equipment Manufacturer – [OEM](/mobilnisite/slovnik/oem/)). Její zařazení slouží pedagogickému a normativnímu účelu, neboť poskytuje konkrétní referenční bod pro diskuse a požadavky související se službami a komunikací založenými na vozidlech. Specifikace používá tuto pojmenovanou entitu k ukotvení abstraktních technických diskusí v rozpoznatelném průmyslovém kontextu, zejména při detailním popisu scénářů pro výkon multimediálních aplikací v prostředí vozidel, což je hlavním předmětem dokumentu TS 26.938.

Účelem takové reference je usnadnit společnou shodu mezi účastníky standardizace a následně mezi implementátory. Při definování výkonnostních metrik, požadavků na latenci nebo potřeb propustnosti dat pro infotainment v vozidle (IVI), pokročilé asistenční systémy řidiče (ADAS) nebo komunikaci vozidlo-síť (V2N) pomáhá použití známé automobilové značky, jako je BMW, kontextualizovat technické parametry. Odpovídá na otázku 'pro koho', čímž zajišťuje, že vyvíjené standardy jsou v souladu s praktickými možnostmi a integračními potřebami skutečných výrobců vozidel. To je klíčové pro zajištění životaschopnosti výsledných funkcí 3GPP pro nasazení v komerčních vozidlech.

Z architektonického hlediska tato reference neimplikuje žádné specifické proprietární rozhraní nebo uzel společnosti BMW v rámci systému 3GPP. Místo toho je vozidlo, reprezentované OEM, považováno za uživatelské zařízení (UE) nebo soubor UE se specifickými form-faktory a podmínkami použití. Normalizační práce zohledňují integrační bod vozidla – palubní jednotku (OBU) nebo telematickou řídicí jednotku (TCU) – která hostí 3GPP modem a provádí protokolový zásobník. Mezi klíčové aspekty ovlivněné takovými příklady OEM patří omezení umístění antény daná designem vozidla, stabilita napájení z elektrického systému vozidla, rozsahy provozních teplot a potřeba spolehlivého připojení navzdory vysokorychlostní mobilitě a proměnlivým rádiovým podmínkám.

Zmínka o BMW v technických specifikacích 3GPP je tedy metodologickým nástrojem pro inženýrství požadavků. Zajišťuje, že návrh celulárního systému – pokrývající aspekty od návrhu vlnové formy fyzické vrstvy až po zpřístupnění služeb jádra sítě pro vozidla – zohledňuje reálné výzvy automobilové integrace. To vede k robustnějším a implementovatelnějším standardům pro C-V2X (Cellular Vehicle-to-Everything), síťově řízené interaktivní služby pro vozidla a správu QoS pro mobilitu, které jsou základem pro služby spojeného a automatizovaného řízení.

## K čemu slouží

Účelem odkazování na konkrétní automobilové výrobce ([OEM](/mobilnisite/slovnik/oem/)), jako je BMW, v technických specifikacích 3GPP je ukotvit vysoce technické systémové požadavky v hmatatelných, reálných scénářích nasazení. Abstraktní údaje o výkonu sítě získávají praktický význam, když jsou spojeny s vozidlovou platformou známého výrobce. Tato praxe byla zvláště motivována průmyslem řízeným tlakem na standardizované celulární řešení pro komunikaci vozidel, které začalo nabírat významnou dynamiku v 3GPP přibližně od vydání 14 se standardizací LTE-V2X. Použití konkrétních příkladů pomáhá překlenout propast mezi telekomunikačními a automobilovými inženýry a zajišťuje, že vyvíjené standardy jsou nejen teoreticky správné, ale také prakticky integrovatelné do procesů návrhu a výroby vozidel.

Historicky, před vznikem specializovaných standardů C-V2X, byla komunikace vozidel závislá na proprietárních řešeních nebo necelulárních technologiích, jako je [IEEE](/mobilnisite/slovnik/ieee/) 802.11p (DSRC), což představovalo výzvy v globální škálovatelnosti, bezproblémové integraci se službami mobilních sítí a možnostech evoluce. Zařazení názvů automobilových OEM do studijních položek a specifikací signalizovalo posun k více kolaborativnímu, meziodvětvovému přístupu standardizace. Řešilo to omezení vytváření standardů zaměřených pouze na síť izolovaně, bez důkladného zohlednění omezení koncového zařízení (vozidla) a jeho provozních profilů. Zvolením konkrétního OEM specifikace implicitně řeší problémy certifikace zařízení, požadavků na hardware automobilové kvality a potřebu předvídatelného chování služeb v náročných podmínkách mobility.

Tato metodologie řeší problém nejednoznačných požadavků. Namísto tvrzení 'síť musí podporovat nízkou latenci pro vozidla' lze kontextualizovanější požadavek formulovat s ohledem na potřeby OEM, jako je BMW, pro konkrétní případ užití, například sdílení senzorových dat pro prevenci kolizí. To vede k přesnější technické práci na časovačích protokolů, plánovacích mechanismech a rámcích QoS. Motivací je v konečném důsledku vytvořit soubor standardů 3GPP, které mohou automobiloví výrobci s důvěrou přijmout, protože vědí, že jejich specifická provozní prostředí a výkonnostní kritéria byla během normalizačního procesu výslovně zohledněna, čímž se urychluje komerční nasazení služeb spojených vozidel.

## Klíčové vlastnosti

- Slouží jako konkrétní reference pro požadavky automobilových OEM v normativním textu
- Kontextualizuje výkonnostní metriky pro případy užití v oblasti vozidel (např. latence, propustnost)
- Ukotvuje diskuse o síťové integraci v vozidle a form-faktorech UE
- Usnadňuje meziodvětvové porozumění mezi telekomunikačním a automobilovým sektorem
- Používá se k odvození reálných scénářů pro studie komunikace V2X
- Pomáhá definovat kanálové modely a podmínky mobility pro testování

## Definující specifikace

- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [BMW na 3GPP Explorer](https://3gpp-explorer.com/glossary/bmw/)
