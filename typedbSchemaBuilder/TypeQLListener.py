# Generated from TypeQL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .TypeQLParser import TypeQLParser
else:
    from TypeQLParser import TypeQLParser

# This class defines a complete listener for a parse tree produced by TypeQLParser.
class TypeQLListener(ParseTreeListener):

    # Enter a parse tree produced by TypeQLParser#eof_query.
    def enterEof_query(self, ctx:TypeQLParser.Eof_queryContext):
        pass

    # Exit a parse tree produced by TypeQLParser#eof_query.
    def exitEof_query(self, ctx:TypeQLParser.Eof_queryContext):
        pass


    # Enter a parse tree produced by TypeQLParser#eof_queries.
    def enterEof_queries(self, ctx:TypeQLParser.Eof_queriesContext):
        pass

    # Exit a parse tree produced by TypeQLParser#eof_queries.
    def exitEof_queries(self, ctx:TypeQLParser.Eof_queriesContext):
        pass


    # Enter a parse tree produced by TypeQLParser#eof_pattern.
    def enterEof_pattern(self, ctx:TypeQLParser.Eof_patternContext):
        pass

    # Exit a parse tree produced by TypeQLParser#eof_pattern.
    def exitEof_pattern(self, ctx:TypeQLParser.Eof_patternContext):
        pass


    # Enter a parse tree produced by TypeQLParser#eof_patterns.
    def enterEof_patterns(self, ctx:TypeQLParser.Eof_patternsContext):
        pass

    # Exit a parse tree produced by TypeQLParser#eof_patterns.
    def exitEof_patterns(self, ctx:TypeQLParser.Eof_patternsContext):
        pass


    # Enter a parse tree produced by TypeQLParser#eof_definables.
    def enterEof_definables(self, ctx:TypeQLParser.Eof_definablesContext):
        pass

    # Exit a parse tree produced by TypeQLParser#eof_definables.
    def exitEof_definables(self, ctx:TypeQLParser.Eof_definablesContext):
        pass


    # Enter a parse tree produced by TypeQLParser#eof_variable.
    def enterEof_variable(self, ctx:TypeQLParser.Eof_variableContext):
        pass

    # Exit a parse tree produced by TypeQLParser#eof_variable.
    def exitEof_variable(self, ctx:TypeQLParser.Eof_variableContext):
        pass


    # Enter a parse tree produced by TypeQLParser#eof_label.
    def enterEof_label(self, ctx:TypeQLParser.Eof_labelContext):
        pass

    # Exit a parse tree produced by TypeQLParser#eof_label.
    def exitEof_label(self, ctx:TypeQLParser.Eof_labelContext):
        pass


    # Enter a parse tree produced by TypeQLParser#eof_schema_rule.
    def enterEof_schema_rule(self, ctx:TypeQLParser.Eof_schema_ruleContext):
        pass

    # Exit a parse tree produced by TypeQLParser#eof_schema_rule.
    def exitEof_schema_rule(self, ctx:TypeQLParser.Eof_schema_ruleContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query.
    def enterQuery(self, ctx:TypeQLParser.QueryContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query.
    def exitQuery(self, ctx:TypeQLParser.QueryContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query_define.
    def enterQuery_define(self, ctx:TypeQLParser.Query_defineContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query_define.
    def exitQuery_define(self, ctx:TypeQLParser.Query_defineContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query_undefine.
    def enterQuery_undefine(self, ctx:TypeQLParser.Query_undefineContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query_undefine.
    def exitQuery_undefine(self, ctx:TypeQLParser.Query_undefineContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query_insert.
    def enterQuery_insert(self, ctx:TypeQLParser.Query_insertContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query_insert.
    def exitQuery_insert(self, ctx:TypeQLParser.Query_insertContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query_update.
    def enterQuery_update(self, ctx:TypeQLParser.Query_updateContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query_update.
    def exitQuery_update(self, ctx:TypeQLParser.Query_updateContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query_delete.
    def enterQuery_delete(self, ctx:TypeQLParser.Query_deleteContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query_delete.
    def exitQuery_delete(self, ctx:TypeQLParser.Query_deleteContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query_match.
    def enterQuery_match(self, ctx:TypeQLParser.Query_matchContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query_match.
    def exitQuery_match(self, ctx:TypeQLParser.Query_matchContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query_match_aggregate.
    def enterQuery_match_aggregate(self, ctx:TypeQLParser.Query_match_aggregateContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query_match_aggregate.
    def exitQuery_match_aggregate(self, ctx:TypeQLParser.Query_match_aggregateContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query_match_group.
    def enterQuery_match_group(self, ctx:TypeQLParser.Query_match_groupContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query_match_group.
    def exitQuery_match_group(self, ctx:TypeQLParser.Query_match_groupContext):
        pass


    # Enter a parse tree produced by TypeQLParser#query_match_group_agg.
    def enterQuery_match_group_agg(self, ctx:TypeQLParser.Query_match_group_aggContext):
        pass

    # Exit a parse tree produced by TypeQLParser#query_match_group_agg.
    def exitQuery_match_group_agg(self, ctx:TypeQLParser.Query_match_group_aggContext):
        pass


    # Enter a parse tree produced by TypeQLParser#modifiers.
    def enterModifiers(self, ctx:TypeQLParser.ModifiersContext):
        pass

    # Exit a parse tree produced by TypeQLParser#modifiers.
    def exitModifiers(self, ctx:TypeQLParser.ModifiersContext):
        pass


    # Enter a parse tree produced by TypeQLParser#filter.
    def enterFilter(self, ctx:TypeQLParser.FilterContext):
        pass

    # Exit a parse tree produced by TypeQLParser#filter.
    def exitFilter(self, ctx:TypeQLParser.FilterContext):
        pass


    # Enter a parse tree produced by TypeQLParser#sort.
    def enterSort(self, ctx:TypeQLParser.SortContext):
        pass

    # Exit a parse tree produced by TypeQLParser#sort.
    def exitSort(self, ctx:TypeQLParser.SortContext):
        pass


    # Enter a parse tree produced by TypeQLParser#var_order.
    def enterVar_order(self, ctx:TypeQLParser.Var_orderContext):
        pass

    # Exit a parse tree produced by TypeQLParser#var_order.
    def exitVar_order(self, ctx:TypeQLParser.Var_orderContext):
        pass


    # Enter a parse tree produced by TypeQLParser#offset.
    def enterOffset(self, ctx:TypeQLParser.OffsetContext):
        pass

    # Exit a parse tree produced by TypeQLParser#offset.
    def exitOffset(self, ctx:TypeQLParser.OffsetContext):
        pass


    # Enter a parse tree produced by TypeQLParser#limit.
    def enterLimit(self, ctx:TypeQLParser.LimitContext):
        pass

    # Exit a parse tree produced by TypeQLParser#limit.
    def exitLimit(self, ctx:TypeQLParser.LimitContext):
        pass


    # Enter a parse tree produced by TypeQLParser#match_aggregate.
    def enterMatch_aggregate(self, ctx:TypeQLParser.Match_aggregateContext):
        pass

    # Exit a parse tree produced by TypeQLParser#match_aggregate.
    def exitMatch_aggregate(self, ctx:TypeQLParser.Match_aggregateContext):
        pass


    # Enter a parse tree produced by TypeQLParser#aggregate_method.
    def enterAggregate_method(self, ctx:TypeQLParser.Aggregate_methodContext):
        pass

    # Exit a parse tree produced by TypeQLParser#aggregate_method.
    def exitAggregate_method(self, ctx:TypeQLParser.Aggregate_methodContext):
        pass


    # Enter a parse tree produced by TypeQLParser#match_group.
    def enterMatch_group(self, ctx:TypeQLParser.Match_groupContext):
        pass

    # Exit a parse tree produced by TypeQLParser#match_group.
    def exitMatch_group(self, ctx:TypeQLParser.Match_groupContext):
        pass


    # Enter a parse tree produced by TypeQLParser#definables.
    def enterDefinables(self, ctx:TypeQLParser.DefinablesContext):
        pass

    # Exit a parse tree produced by TypeQLParser#definables.
    def exitDefinables(self, ctx:TypeQLParser.DefinablesContext):
        pass


    # Enter a parse tree produced by TypeQLParser#definable.
    def enterDefinable(self, ctx:TypeQLParser.DefinableContext):
        pass

    # Exit a parse tree produced by TypeQLParser#definable.
    def exitDefinable(self, ctx:TypeQLParser.DefinableContext):
        pass


    # Enter a parse tree produced by TypeQLParser#patterns.
    def enterPatterns(self, ctx:TypeQLParser.PatternsContext):
        pass

    # Exit a parse tree produced by TypeQLParser#patterns.
    def exitPatterns(self, ctx:TypeQLParser.PatternsContext):
        pass


    # Enter a parse tree produced by TypeQLParser#pattern.
    def enterPattern(self, ctx:TypeQLParser.PatternContext):
        pass

    # Exit a parse tree produced by TypeQLParser#pattern.
    def exitPattern(self, ctx:TypeQLParser.PatternContext):
        pass


    # Enter a parse tree produced by TypeQLParser#pattern_conjunction.
    def enterPattern_conjunction(self, ctx:TypeQLParser.Pattern_conjunctionContext):
        pass

    # Exit a parse tree produced by TypeQLParser#pattern_conjunction.
    def exitPattern_conjunction(self, ctx:TypeQLParser.Pattern_conjunctionContext):
        pass


    # Enter a parse tree produced by TypeQLParser#pattern_disjunction.
    def enterPattern_disjunction(self, ctx:TypeQLParser.Pattern_disjunctionContext):
        pass

    # Exit a parse tree produced by TypeQLParser#pattern_disjunction.
    def exitPattern_disjunction(self, ctx:TypeQLParser.Pattern_disjunctionContext):
        pass


    # Enter a parse tree produced by TypeQLParser#pattern_negation.
    def enterPattern_negation(self, ctx:TypeQLParser.Pattern_negationContext):
        pass

    # Exit a parse tree produced by TypeQLParser#pattern_negation.
    def exitPattern_negation(self, ctx:TypeQLParser.Pattern_negationContext):
        pass


    # Enter a parse tree produced by TypeQLParser#pattern_variable.
    def enterPattern_variable(self, ctx:TypeQLParser.Pattern_variableContext):
        pass

    # Exit a parse tree produced by TypeQLParser#pattern_variable.
    def exitPattern_variable(self, ctx:TypeQLParser.Pattern_variableContext):
        pass


    # Enter a parse tree produced by TypeQLParser#variable_concept.
    def enterVariable_concept(self, ctx:TypeQLParser.Variable_conceptContext):
        pass

    # Exit a parse tree produced by TypeQLParser#variable_concept.
    def exitVariable_concept(self, ctx:TypeQLParser.Variable_conceptContext):
        pass


    # Enter a parse tree produced by TypeQLParser#variable_type.
    def enterVariable_type(self, ctx:TypeQLParser.Variable_typeContext):
        pass

    # Exit a parse tree produced by TypeQLParser#variable_type.
    def exitVariable_type(self, ctx:TypeQLParser.Variable_typeContext):
        pass


    # Enter a parse tree produced by TypeQLParser#type_constraint.
    def enterType_constraint(self, ctx:TypeQLParser.Type_constraintContext):
        pass

    # Exit a parse tree produced by TypeQLParser#type_constraint.
    def exitType_constraint(self, ctx:TypeQLParser.Type_constraintContext):
        pass


    # Enter a parse tree produced by TypeQLParser#annotations_owns.
    def enterAnnotations_owns(self, ctx:TypeQLParser.Annotations_ownsContext):
        pass

    # Exit a parse tree produced by TypeQLParser#annotations_owns.
    def exitAnnotations_owns(self, ctx:TypeQLParser.Annotations_ownsContext):
        pass


    # Enter a parse tree produced by TypeQLParser#variable_value.
    def enterVariable_value(self, ctx:TypeQLParser.Variable_valueContext):
        pass

    # Exit a parse tree produced by TypeQLParser#variable_value.
    def exitVariable_value(self, ctx:TypeQLParser.Variable_valueContext):
        pass


    # Enter a parse tree produced by TypeQLParser#variable_things.
    def enterVariable_things(self, ctx:TypeQLParser.Variable_thingsContext):
        pass

    # Exit a parse tree produced by TypeQLParser#variable_things.
    def exitVariable_things(self, ctx:TypeQLParser.Variable_thingsContext):
        pass


    # Enter a parse tree produced by TypeQLParser#variable_thing_any.
    def enterVariable_thing_any(self, ctx:TypeQLParser.Variable_thing_anyContext):
        pass

    # Exit a parse tree produced by TypeQLParser#variable_thing_any.
    def exitVariable_thing_any(self, ctx:TypeQLParser.Variable_thing_anyContext):
        pass


    # Enter a parse tree produced by TypeQLParser#variable_thing.
    def enterVariable_thing(self, ctx:TypeQLParser.Variable_thingContext):
        pass

    # Exit a parse tree produced by TypeQLParser#variable_thing.
    def exitVariable_thing(self, ctx:TypeQLParser.Variable_thingContext):
        pass


    # Enter a parse tree produced by TypeQLParser#variable_relation.
    def enterVariable_relation(self, ctx:TypeQLParser.Variable_relationContext):
        pass

    # Exit a parse tree produced by TypeQLParser#variable_relation.
    def exitVariable_relation(self, ctx:TypeQLParser.Variable_relationContext):
        pass


    # Enter a parse tree produced by TypeQLParser#variable_attribute.
    def enterVariable_attribute(self, ctx:TypeQLParser.Variable_attributeContext):
        pass

    # Exit a parse tree produced by TypeQLParser#variable_attribute.
    def exitVariable_attribute(self, ctx:TypeQLParser.Variable_attributeContext):
        pass


    # Enter a parse tree produced by TypeQLParser#relation.
    def enterRelation(self, ctx:TypeQLParser.RelationContext):
        pass

    # Exit a parse tree produced by TypeQLParser#relation.
    def exitRelation(self, ctx:TypeQLParser.RelationContext):
        pass


    # Enter a parse tree produced by TypeQLParser#role_player.
    def enterRole_player(self, ctx:TypeQLParser.Role_playerContext):
        pass

    # Exit a parse tree produced by TypeQLParser#role_player.
    def exitRole_player(self, ctx:TypeQLParser.Role_playerContext):
        pass


    # Enter a parse tree produced by TypeQLParser#player.
    def enterPlayer(self, ctx:TypeQLParser.PlayerContext):
        pass

    # Exit a parse tree produced by TypeQLParser#player.
    def exitPlayer(self, ctx:TypeQLParser.PlayerContext):
        pass


    # Enter a parse tree produced by TypeQLParser#attributes.
    def enterAttributes(self, ctx:TypeQLParser.AttributesContext):
        pass

    # Exit a parse tree produced by TypeQLParser#attributes.
    def exitAttributes(self, ctx:TypeQLParser.AttributesContext):
        pass


    # Enter a parse tree produced by TypeQLParser#attribute.
    def enterAttribute(self, ctx:TypeQLParser.AttributeContext):
        pass

    # Exit a parse tree produced by TypeQLParser#attribute.
    def exitAttribute(self, ctx:TypeQLParser.AttributeContext):
        pass


    # Enter a parse tree produced by TypeQLParser#predicate.
    def enterPredicate(self, ctx:TypeQLParser.PredicateContext):
        pass

    # Exit a parse tree produced by TypeQLParser#predicate.
    def exitPredicate(self, ctx:TypeQLParser.PredicateContext):
        pass


    # Enter a parse tree produced by TypeQLParser#predicate_equality.
    def enterPredicate_equality(self, ctx:TypeQLParser.Predicate_equalityContext):
        pass

    # Exit a parse tree produced by TypeQLParser#predicate_equality.
    def exitPredicate_equality(self, ctx:TypeQLParser.Predicate_equalityContext):
        pass


    # Enter a parse tree produced by TypeQLParser#predicate_substring.
    def enterPredicate_substring(self, ctx:TypeQLParser.Predicate_substringContext):
        pass

    # Exit a parse tree produced by TypeQLParser#predicate_substring.
    def exitPredicate_substring(self, ctx:TypeQLParser.Predicate_substringContext):
        pass


    # Enter a parse tree produced by TypeQLParser#predicate_value.
    def enterPredicate_value(self, ctx:TypeQLParser.Predicate_valueContext):
        pass

    # Exit a parse tree produced by TypeQLParser#predicate_value.
    def exitPredicate_value(self, ctx:TypeQLParser.Predicate_valueContext):
        pass


    # Enter a parse tree produced by TypeQLParser#expression.
    def enterExpression(self, ctx:TypeQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TypeQLParser#expression.
    def exitExpression(self, ctx:TypeQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TypeQLParser#expression_base.
    def enterExpression_base(self, ctx:TypeQLParser.Expression_baseContext):
        pass

    # Exit a parse tree produced by TypeQLParser#expression_base.
    def exitExpression_base(self, ctx:TypeQLParser.Expression_baseContext):
        pass


    # Enter a parse tree produced by TypeQLParser#expression_function.
    def enterExpression_function(self, ctx:TypeQLParser.Expression_functionContext):
        pass

    # Exit a parse tree produced by TypeQLParser#expression_function.
    def exitExpression_function(self, ctx:TypeQLParser.Expression_functionContext):
        pass


    # Enter a parse tree produced by TypeQLParser#expression_function_name.
    def enterExpression_function_name(self, ctx:TypeQLParser.Expression_function_nameContext):
        pass

    # Exit a parse tree produced by TypeQLParser#expression_function_name.
    def exitExpression_function_name(self, ctx:TypeQLParser.Expression_function_nameContext):
        pass


    # Enter a parse tree produced by TypeQLParser#expression_arguments.
    def enterExpression_arguments(self, ctx:TypeQLParser.Expression_argumentsContext):
        pass

    # Exit a parse tree produced by TypeQLParser#expression_arguments.
    def exitExpression_arguments(self, ctx:TypeQLParser.Expression_argumentsContext):
        pass


    # Enter a parse tree produced by TypeQLParser#schema_rule.
    def enterSchema_rule(self, ctx:TypeQLParser.Schema_ruleContext):
        pass

    # Exit a parse tree produced by TypeQLParser#schema_rule.
    def exitSchema_rule(self, ctx:TypeQLParser.Schema_ruleContext):
        pass


    # Enter a parse tree produced by TypeQLParser#type_any.
    def enterType_any(self, ctx:TypeQLParser.Type_anyContext):
        pass

    # Exit a parse tree produced by TypeQLParser#type_any.
    def exitType_any(self, ctx:TypeQLParser.Type_anyContext):
        pass


    # Enter a parse tree produced by TypeQLParser#type_scoped.
    def enterType_scoped(self, ctx:TypeQLParser.Type_scopedContext):
        pass

    # Exit a parse tree produced by TypeQLParser#type_scoped.
    def exitType_scoped(self, ctx:TypeQLParser.Type_scopedContext):
        pass


    # Enter a parse tree produced by TypeQLParser#type.
    def enterType(self, ctx:TypeQLParser.TypeContext):
        pass

    # Exit a parse tree produced by TypeQLParser#type.
    def exitType(self, ctx:TypeQLParser.TypeContext):
        pass


    # Enter a parse tree produced by TypeQLParser#label_any.
    def enterLabel_any(self, ctx:TypeQLParser.Label_anyContext):
        pass

    # Exit a parse tree produced by TypeQLParser#label_any.
    def exitLabel_any(self, ctx:TypeQLParser.Label_anyContext):
        pass


    # Enter a parse tree produced by TypeQLParser#label_scoped.
    def enterLabel_scoped(self, ctx:TypeQLParser.Label_scopedContext):
        pass

    # Exit a parse tree produced by TypeQLParser#label_scoped.
    def exitLabel_scoped(self, ctx:TypeQLParser.Label_scopedContext):
        pass


    # Enter a parse tree produced by TypeQLParser#label.
    def enterLabel(self, ctx:TypeQLParser.LabelContext):
        pass

    # Exit a parse tree produced by TypeQLParser#label.
    def exitLabel(self, ctx:TypeQLParser.LabelContext):
        pass


    # Enter a parse tree produced by TypeQLParser#type_native.
    def enterType_native(self, ctx:TypeQLParser.Type_nativeContext):
        pass

    # Exit a parse tree produced by TypeQLParser#type_native.
    def exitType_native(self, ctx:TypeQLParser.Type_nativeContext):
        pass


    # Enter a parse tree produced by TypeQLParser#value_type.
    def enterValue_type(self, ctx:TypeQLParser.Value_typeContext):
        pass

    # Exit a parse tree produced by TypeQLParser#value_type.
    def exitValue_type(self, ctx:TypeQLParser.Value_typeContext):
        pass


    # Enter a parse tree produced by TypeQLParser#value.
    def enterValue(self, ctx:TypeQLParser.ValueContext):
        pass

    # Exit a parse tree produced by TypeQLParser#value.
    def exitValue(self, ctx:TypeQLParser.ValueContext):
        pass


    # Enter a parse tree produced by TypeQLParser#signed_long.
    def enterSigned_long(self, ctx:TypeQLParser.Signed_longContext):
        pass

    # Exit a parse tree produced by TypeQLParser#signed_long.
    def exitSigned_long(self, ctx:TypeQLParser.Signed_longContext):
        pass


    # Enter a parse tree produced by TypeQLParser#signed_double.
    def enterSigned_double(self, ctx:TypeQLParser.Signed_doubleContext):
        pass

    # Exit a parse tree produced by TypeQLParser#signed_double.
    def exitSigned_double(self, ctx:TypeQLParser.Signed_doubleContext):
        pass


    # Enter a parse tree produced by TypeQLParser#sign.
    def enterSign(self, ctx:TypeQLParser.SignContext):
        pass

    # Exit a parse tree produced by TypeQLParser#sign.
    def exitSign(self, ctx:TypeQLParser.SignContext):
        pass


    # Enter a parse tree produced by TypeQLParser#unreserved.
    def enterUnreserved(self, ctx:TypeQLParser.UnreservedContext):
        pass

    # Exit a parse tree produced by TypeQLParser#unreserved.
    def exitUnreserved(self, ctx:TypeQLParser.UnreservedContext):
        pass



del TypeQLParser