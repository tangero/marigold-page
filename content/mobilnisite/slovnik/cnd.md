---
slug: "cnd"
url: "/mobilnisite/slovnik/cnd/"
type: "slovnik"
title: "CND – Customer Network Device"
date: 2025-01-01
abbr: "CND"
fullName: "Customer Network Device"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cnd/"
summary: "Customer Network Device (CND, česky zákaznické síťové zařízení) je uživatelské zařízení nebo síťový prvek umístěný v prostorách zákazníka, který se připojuje k síti 3GPP. Umožňuje rezidenčním nebo pod"
---

CND je uživatelské zařízení nebo síťový prvek umístěný v prostorách zákazníka, který se připojuje k síti 3GPP, aby propojil zákaznické sítě s infrastrukturou operátora.

## Popis

Customer Network Device (CND) představuje jakékoli koncové zařízení nebo síťovou komponentu umístěnou v lokalitě zákazníka, která rozhraní s infrastrukturou sítě 3GPP. Podle specifikací 3GPP, zejména TS 24.523, zahrnují CND širokou kategorii zařízení včetně rezidenčních bran, podnikových směrovačů, bran IoT a specializovaných uživatelských zařízení, která navazují konektivitu mezi sítěmi v prostorách zákazníka a jádrovou sítí mobilního operátora. Tato zařízení slouží jako fyzické a logické hraniční body, kde se zákaznické nebo zákazníkem spravované sítě setkávají se standardizovanou mobilní infrastrukturou operátora.

Architektonicky CND implementují specifické protokoly a rozhraní 3GPP pro komunikaci se síťovými funkcemi v řídicí i uživatelské rovině. Typicky obsahují moduly pro rádiový přístup (pokud je zahrnuto bezdrátové připojení), překlad síťových adres, funkce firewallu, správu kvality služeb a autentizační mechanismy. Zařízení musí podporovat standardizované procedury pro připojení, autentizaci, navázání relace a správu mobility, jak jsou definovány ve specifikacích 3GPP. Z pohledu sítě jsou CND považovány za důvěryhodné koncové body, které dodržují politiky operátora a zároveň poskytují služby koncovým uživatelům v rámci zákaznické sítě.

Klíčové komponenty CND zahrnují moduly síťového rozhraní (které mohou podporovat více technologií rádiového přístupu), implementaci protokolového zásobníku (včetně vrstev [NAS](/mobilnisite/slovnik/nas/), [RRC](/mobilnisite/slovnik/rrc/) a IP), bezpečnostní moduly pro autentizaci a šifrování a rozhraní pro správu pro konfiguraci a monitorování. Zařízení funguje tak, že navazuje zabezpečené tunely k síťovým branám, implementuje body vynucování politik pro správu provozu a poskytuje služby konektivity podřízeným zařízením. V podnikových scénářích mohou CND implementovat další funkce, jako je ukončení VPN, místní breakout nebo směrování specifické pro aplikace.

Role CND v síťovém ekosystému je mnohostranná: rozšiřují dosah mobilních sítí do pevných lokalit, umožňují konvergované služby napříč přístupovými technologiemi a poskytují spravovaný bod rozhraní pro doručování služeb. Operátoři mohou prostřednictvím těchto standardizovaných zařízení umístěných u zákazníka nasazovat služby, uplatňovat politiky a sbírat metriky. Pro zákazníky CND nabízejí konzistentní zážitek při přístupu ke službám mobilní sítě z pevných lokalit s přidaným benefitem integrace s místní sítí a potenciálně vylepšeného výkonu díky lokalizovanému zpracování a možnostem ukládání do mezipaměti.

## K čemu slouží

Koncept Customer Network Device byl zaveden, aby řešil rostoucí potřebu bezproblémové integrace mezi zařízeními v prostorách zákazníka a mobilními sítěmi 3GPP. Jak telekomunikace směřovaly ke konvergenci pevných a mobilních sítí, operátoři potřebovali standardizované přístupy pro rozšíření mobilních služeb do rezidenčních a podnikových prostředí. Předchozí přístupy se spoléhaly na proprietární řešení nebo vyžadovaly, aby zákazníci používali obecná uživatelská zařízení, která postrádala schopnosti potřebné pro síťovou integraci ve velkém měřítku.

Historicky byla zařízení zákazníků připojující se k mobilním sítím omezena na telefony nebo modemy s minimálními síťovými schopnostmi. Vzestup chytrých domácností, podnikové mobility a nasazení IoT vytvořil poptávku po sofistikovanějších zařízeních umístěných u zákazníka, která by mohla sloužit jako brány pro více podřízených zařízení při zachování zabezpečených, politikami řízených připojení k mobilní síti. Specifikace CND poskytla standardizovaný rámec pro taková zařízení, což umožnilo interoperabilitu mezi zařízeními od různých dodavatelů a konzistentní doručování služeb napříč sítěmi operátorů.

Zavedení CND ve vydání 12 řešilo omezení předchozích přístupů definováním jasných architektonických hranic, standardizovaných rozhraní a společných funkčních požadavků. To umožnilo operátorům nasazovat přidané služby prostřednictvím zařízení umístěných u zákazníka při zachování síťové bezpečnosti a kvality služeb. Specifikace také usnadnila nové obchodní modely, kde operátoři mohli poskytovat spravovaná CND zákazníkům jako součást servisních balíčků, čímž vytvářeli další zdroje příjmů a zároveň zlepšovali zákaznický zážitek díky lepší integraci mezi mobilními a pevnými sítěmi.

## Klíčové vlastnosti

- Standardizované rozhraní k jádrové síti 3GPP
- Podpora více přístupových technologií včetně LTE a 5G NR
- Integrované autentizační a bezpečnostní mechanismy
- Správa kvality služeb a vynucování politik
- Schopnosti překladu síťových adres a firewallu
- Rozhraní pro vzdálenou správu a konfiguraci

## Definující specifikace

- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios

---

📖 **Anglický originál a plná specifikace:** [CND na 3GPP Explorer](https://3gpp-explorer.com/glossary/cnd/)
