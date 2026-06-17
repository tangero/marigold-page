---
slug: "abmf"
url: "/mobilnisite/slovnik/abmf/"
type: "slovnik"
title: "ABMF – Accounting Balance Management Function"
date: 2026-01-01
abbr: "ABMF"
fullName: "Accounting Balance Management Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/abmf/"
summary: "ABMF je klíčová komponenta účtovacího a fakturačního systému 3GPP, konkrétně v rámci online účtovacího systému (OCS). Spravuje zůstatky na účtech účastníků v reálném čase, sleduje jednotky kreditu (pe"
---

ABMF je funkce správy účetního zůstatku (Accounting Balance Management Function), klíčová komponenta online účtovacího systému (Online Charging System), která spravuje zůstatky na účtech účastníků v reálném čase, aby na základě dostupného kreditu autorizovala nebo zamítla poskytnutí služby.

## Popis

Funkce správy účetního zůstatku (Accounting Balance Management Function, ABMF) je základní entita v architektuře online účtovacího systému (Online Charging System, [OCS](/mobilnisite/slovnik/ocs/)) dle specifikací 3GPP, definovaná v telekomunikačních specifikacích pro správu (TS řada 32). Funguje jako centrální úložiště a správce zůstatků na účtech účastníků. Tyto zůstatky nejsou omezeny pouze na peněžní kredit; mohou reprezentovat i nepeněžní jednotky, jako je objem dat, počet SMS nebo přidělené kvóty pro konkrétní služby, což umožňuje flexibilní tarifní a účtovací modely. Primární rolí ABMF je udržovat přesný pohled na dostupné zdroje účastníka v reálném čase, což je nezbytné pro účtování na základě relací, událostí nebo datových toků.

Z architektonického hlediska ABMF komunikuje s dalšími komponentami OCS, především s funkcí správy zůstatků relace (Session Balance Management Function, SBMF) a s tarifní funkcí (Rating Function, RF). Když je zahájena žádost o službu, centrální funkce OCS, často Online Charging Function ([OCF](/mobilnisite/slovnik/ocf/)), se dotazuje přes SBMF na ABMF, aby zkontrolovala zůstatek účastníka a rezervovala potřebné jednotky pro požadovanou službu. ABMF provádí atomické operace – odečtení (debit), přičtení (credit), rezervaci (reserve) a uvolnění (release) – se zůstatkem, čímž zajišťuje konzistenci dat a předchází stavům soutěže v prostředí vícevláknového účtování. Spravuje zůstatky pro každého účastníka, které mohou být dále členěny na více typů (např. propagační zůstatek, hlavní zůstatek) a kategorií.

ABMF funguje tak, že zpracovává požadavky na správu zůstatku přes standardizovaná rozhraní, primárně v rámci OCS. Ukládá informace o zůstatku, které zahrnují aktuální hodnotu, dobu platnosti a související prahové hodnoty. Když je provedena rezervace, ABMF odečte rezervovanou částku z dostupného zůstatku a drží ji, dokud není služba spotřebována nebo zrušena. Po obdržení hlášení o skutečném využití ze sítě ABMF dokončí transakci převodem rezervace na trvalé odepsání nebo uvolněním nevyužitých částí zpět do dostupného zůstatku. Tento proces dvoufázového potvrzení (two-phase commit) je klíčový pro přesné účtování a prevenci překročení limitu.

Její role přesahuje pouhé sledování zůstatku; ABMF podporuje komplexní funkce, jako je sdílení zůstatku mezi více účastníky (rodinné tarify), převody zůstatků a dobíjení zůstatků. Také vynucuje limity zůstatků a spouští notifikace, když zůstatky poklesnou pod předdefinované prahové hodnoty, což lze využít k vyvolání výzvy k dobíjení nebo snížení kvality služby. ABMF je navržena pro vysokou dostupnost a spolehlivost, protože jakékoli selhání by mohlo vést ke ztrátě výnosů nebo narušení služeb. Jde o stavovou komponentu, která musí zvládat souběžné transakce od milionů účastníků, což činí její výkon a škálovatelnost pro síťové operátory zásadními.

## K čemu slouží

ABMF byla vytvořena, aby řešila základní potřebu správy zůstatků v reálném čase a spolehlivým způsobem v telekomunikačních sítích, zejména s nástupem předplacených služeb. Před standardizací online účtování byly předplacené systémy často proprietární a izolované, což ztěžovalo nabídku konvergentních služeb (např. hlas, data a zasílání zpráv na jeden zůstatek) nebo integraci s moderními službami založenými na IP. ABMF jako součást architektury [OCS](/mobilnisite/slovnik/ocs/) 3GPP, představené ve vydání 5 a upravené ve vydání 8, poskytuje standardizovaný, robustní mechanismus pro konzistentní správu zůstatků na účtech účastníků napříč všemi službami.

Řeší problém zajištění výnosů tím, že zajišťuje autorizaci využití služby pouze při dostatečném zůstatku, čímž předchází vzniku nedobytných pohledávek. Dále umožňuje sofistikované obchodní modely, jako jsou limity pro kontrolu výdajů u uživatelů s účtem (postpaid), propagační nabídky s nepeněžními zůstatky a aktualizace zůstatku v reálném čase. Motivací pro její vývoj byly požadavky operátorů na snížení podvodů, zlepšení zákaznické zkušenosti s okamžitou zpětnou vazbou o zůstatku a podporu konvergence předplaceného a účtovaného (postpaid) paradigmatu do jednoho flexibilního systému.

Historicky byla správa zůstatků často řešena externími, dodavatelsky specifickými platformami pro předplacené služby, kterým chyběla interoperabilita. Standardizace ABMF v rámci frameworku OCS ze strany 3GPP umožnila kompatibilitu mezi více dodavateli, snadnější integraci se síťovými prvky a schopnost rychle podporovat nové služby. Odstranila omezení předchozích přístupů tím, že poskytla centralizované, standardizované úložiště zůstatků, které mohlo být v reálném čase přístupné jakékoli síťové funkci vyžadující autorizaci pro účtování, což umožnilo skutečnou konvergenci a inovativní účtovací strategie.

## Klíčové vlastnosti

- Správa zůstatků v reálném čase pro peněžní i nepeněžní jednotky kreditu
- Podpora atomických operací se zůstatkem (odečtení, přičtení, rezervace, uvolnění) pro zajištění konzistence
- Správa více typů a kategorií zůstatků na jednoho účastníka
- Možnosti sdílení a převodu zůstatku pro skupinové nebo rodinné tarify
- Monitorování prahových hodnot a spouštění notifikací pro varování při nízkém zůstatku
- Návrh pro vysokou dostupnost a škálovatelnost za účelem zvládnutí souběžných transakcí od milionů uživatelů

## Definující specifikace

- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 32.825** (Rel-10) — Study on Rc Reference Point for ABMF

---

📖 **Anglický originál a plná specifikace:** [ABMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/abmf/)
